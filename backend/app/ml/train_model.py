# ==========================================
# Crop Yield Prediction Model Training
# ==========================================

import pandas as pd
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    root_mean_squared_error
)

# Load Dataset
df = pd.read_csv("dataset/dataset_file/yield_df.csv")

# Remove unwanted column
df = df.drop("Unnamed: 0", axis=1)

# Features
X = df.drop("hg/ha_yield", axis=1)

# Target
y = df["hg/ha_yield"]

# Categorical Features
categorical_features = [
    "Area",
    "Item"
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

# Transform
X_processed = preprocessor.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X_processed,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestRegressor(
    n_estimators=50,
    random_state=42,
    n_jobs=-1
)
# Train
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Metrics
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = root_mean_squared_error(y_test, y_pred)

print(f"R2 Score : {r2:.4f}")
print(f"MAE      : {mae:.2f}")
print(f"RMSE     : {rmse:.2f}")

# Save Model
joblib.dump(
    model,
    "backend/app/ml/model.pkl"
)

print("Model Saved Successfully")