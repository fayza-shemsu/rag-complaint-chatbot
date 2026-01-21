import pandas as pd

df = pd.read_csv("data/processed/filtered_complaints.csv")

SAMPLE_SIZE = 12000

sampled_df = (
    df.groupby("Product", group_keys=False)
      .apply(lambda x: x.sample(
          int(SAMPLE_SIZE * len(x) / len(df)),
          random_state=42
      ))
)

sampled_df.to_csv("data/processed/sample_complaints.csv", index=False)
