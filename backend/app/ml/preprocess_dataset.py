# ==========================================
# Dataset Preprocessing
# ==========================================

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import joblib

# Load Dataset
df = pd.read_csv("dataset/dataset_file/yield_df.csv")

# Remove useless column
df = df.drop("Unnamed: 0", axis=1)

# Features
X = df.drop("hg/ha_yield", axis=1)

# Target
y = df["hg/ha_yield"]

# Categorical Columns
categorical_features = [
    "Area",
    "Item"
]

# Numerical Columns
numerical_features = [
    "Year",
    "average_rain_fall_mm_per_year",
    "pesticides_tonnes",
    "avg_temp"
]

# Preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)

# Fit Transform
X_processed = preprocessor.fit_transform(X)

print("Original Shape:", X.shape)
print("Processed Shape:", X_processed.shape)

# Save Preprocessor
joblib.dump(
    preprocessor,
    "backend/app/ml/preprocessor.pkl"
)

print("Preprocessor Saved Successfully")