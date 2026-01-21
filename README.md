Intelligent Complaint Analysis for Financial Services
A Retrieval-Augmented Generation (RAG) Prototype

Project Overview

CrediTrust Financial is a fast-growing digital finance company operating across East African markets. With hundreds of thousands of users across products such as Credit Cards, Personal Loans, Savings Accounts, and Money Transfers, the company receives a high volume of unstructured customer complaints.

Manually analyzing these complaints is time-consuming and inefficient for internal teams such as Product Management, Customer Support, and Compliance.

This project builds an intelligent complaint analysis system that transforms raw customer complaint narratives into a searchable, structured knowledge base using semantic search. The system is designed to later support a Retrieval-Augmented Generation (RAG) chatbot that allows internal stakeholders to ask natural-language questions and receive evidence-backed insights from real complaint data.

Business Objective

The primary goal of this project is to enable internal teams at CrediTrust Financial to:

Rapidly identify recurring customer pain points across financial products

Reduce the time required to detect emerging complaint trends

Empower non-technical users to query large volumes of unstructured complaint data

Shift from reactive issue handling to proactive, data-driven decision making

Solution Approach

The solution follows a RAG-style architecture, implemented in multiple stages:

Exploratory Data Analysis & Preprocessing
Understand complaint distributions, clean raw narratives, and prepare data for downstream NLP tasks.

Text Chunking & Embedding (Semantic Indexing)
Split long complaint narratives into smaller chunks, convert them into vector embeddings, and store them in a vector database for efficient similarity search.

(Planned) RAG Pipeline & Chat Interface
Combine vector retrieval with a language model to generate concise, grounded answers to user questions.

⚠️ Note: This repository currently covers Task 1 and Task 2 (Interim Submission). Tasks 3 and 4 will be implemented in the final phase.

📂 Project Structure
rag-complaint-chatbot/
├── data/
│   ├── raw/                 # Raw CFPB complaint data (ignored by Git)
│   └── processed/           # Cleaned and sampled datasets
├── notebooks/
│   └── 01_eda_preprocessing.ipynb
├── src/
│   ├── preprocess.py        # Data filtering and sampling
│   ├── chunking.py          # Text chunking logic
│   └── embedding_indexing.py# Embedding generation and FAISS indexing
├── vector_store/
│   └── faiss/               # Persisted FAISS index (local only)
├── README.md
├── requirements.txt
└── .gitignore

Dataset

This project uses customer complaint data from the Consumer Financial Protection Bureau (CFPB).

Each complaint record includes:

Product category

Issue and sub-issue labels

Free-text customer complaint narrative

Company and submission metadata

For this project:

Only complaints related to Credit Cards, Personal Loans, Savings Accounts, and Money Transfers are included.

Complaints without narratives are removed.

Large raw datasets and prebuilt embeddings are intentionally excluded from GitHub.

⚙️ Technical Stack

Python 3.10+

Pandas & NumPy – data manipulation

Matplotlib – exploratory visualization

LangChain – text chunking utilities

Sentence-Transformers – semantic embeddings

Model: all-MiniLM-L6-v2

FAISS – vector similarity search

Jupyter Notebook – EDA and analysis

Git & GitHub – version control

🧩 Task 1: EDA & Data Preprocessing (Completed)

Key steps:

Loaded and explored the full CFPB complaint dataset

Analyzed complaint distribution across products

Examined complaint narrative length and variability

Filtered relevant product categories

Removed empty or invalid complaint narratives

Cleaned complaint text to improve embedding quality

Saved the cleaned dataset for downstream processing

All analysis is documented in:

notebooks/01_eda_preprocessing.ipynb

🔗 Task 2: Chunking, Embedding & Vector Indexing (Completed)

Key steps:

Created a stratified sample of ~12,000 complaints to ensure balanced product representation

Implemented text chunking using:

Chunk size: 500 characters

Chunk overlap: 50 characters

Generated semantic embeddings using all-MiniLM-L6-v2

Stored embeddings and metadata in a FAISS vector index

This enables efficient semantic similarity search over complaint narratives.

🚧 Next Steps (Final Submission)

Load the prebuilt full-scale vector store

Implement the RAG retrieval and generation pipeline

Design robust prompts for grounded responses

Evaluate the system using representative business questions

Build an interactive Gradio or Streamlit chat interface

Document results in a final technical report

 Notes

Large datasets and vector indexes are excluded from GitHub via .gitignore

This repository emphasizes clarity, reproducibility, and professional engineering practices

The project is developed as part of the 10 Academy – Artificial Intelligence Mastery Program 

 Author

Fayza Shemsu
AI & Data Engineering Trainee
10 Academy
