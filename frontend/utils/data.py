# ==========================================
# Dataset Dropdown Data
# ==========================================

import pandas as pd

df = pd.read_csv(
    "dataset/dataset_file/yield_df.csv"
)

COUNTRIES = sorted(
    df["Area"].dropna().unique().tolist()
)

CROPS = sorted(
    df["Item"].dropna().unique().tolist()
)