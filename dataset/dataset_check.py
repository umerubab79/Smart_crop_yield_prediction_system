import pandas as pd

files = [
    "dataset/dataset_file/yield.csv",
    "dataset/dataset_file/rainfall.csv",
    "dataset/dataset_file/temp.csv",
    "dataset/dataset_file/pesticides.csv",
    "dataset/dataset_file/yield_df.csv"
]

for file in files:
    print("\n" + "=" * 60)
    print("FILE:", file)

    df = pd.read_csv(file)

    print("Shape:", df.shape)
    print("Columns:")
    print(df.columns.tolist())

    print("\nFirst 3 Rows:")
    print(df.head(3))
    print('==============isnull values=========')
    print(df.isnull().sum())