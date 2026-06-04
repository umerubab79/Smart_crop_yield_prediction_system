import pandas as pd

df = pd.read_csv("dataset/dataset_file/yield_df.csv")

print("Countries:")
print(df["Area"].nunique())

print("\nSample Countries:")
print(df["Area"].unique()[:20])

print("\nCrops:")
print(df["Item"].nunique())

print("\nSample Crops:")
print(df["Item"].unique()[:20])