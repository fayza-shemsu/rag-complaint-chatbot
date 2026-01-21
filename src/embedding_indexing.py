import pandas as pd
from sentence_transformers import SentenceTransformer
from chunking import chunk_text
import faiss
import numpy as np
import pickle
import os

# Load sampled complaints
df = pd.read_csv("data/processed/sample_complaints.csv")

# Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

texts = []
metadata = []

for _, row in df.iterrows():
    chunks = chunk_text(row["clean_narrative"])
    for chunk in chunks:
        texts.append(chunk)
        metadata.append({
            "complaint_id": row.get("Complaint ID", None),
            "product": row["Product"]
        })

print(f"Total chunks created: {len(texts)}")
embeddings = model.encode(texts, show_progress_bar=True)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

print("FAISS index size:", index.ntotal)
os.makedirs("vector_store/faiss", exist_ok=True)

faiss.write_index(index, "vector_store/faiss/index.faiss")

with open("vector_store/faiss/metadata.pkl", "wb") as f:
    pickle.dump(metadata, f)

print("Vector store saved successfully")
