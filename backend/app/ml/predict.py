import pandas as pd
import joblib

# Load saved files
model = joblib.load("backend/app/ml/model.pkl")
preprocessor = joblib.load("backend/app/ml/preprocessor.pkl")

# Sample Input
input_data = pd.DataFrame({
    "Area": ["Pakistan"],
    "Item": ["Wheat"],
    "Year": [2026],
    "average_rain_fall_mm_per_year": [300],
    "pesticides_tonnes": [150],
    "avg_temp": [28]
})

# Transform
processed_data = preprocessor.transform(input_data)

# Predict
prediction = model.predict(processed_data)

print(f"Predicted Yield: {prediction[0]:.2f}")