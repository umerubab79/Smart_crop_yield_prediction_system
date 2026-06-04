import joblib
import pandas as pd

from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.app.schemas.prediction_schema import PredictionInput

from backend.app.database.connection import get_db
from backend.app.database.crud import save_prediction
from backend.app.database.crud import get_predictions

router = APIRouter()


# ==========================================
# Load ML Files
# ==========================================

model = joblib.load(
    "backend/app/ml/model.pkl"
)

preprocessor = joblib.load(
    "backend/app/ml/preprocessor.pkl"
)


# ==========================================
# Predict Crop Yield
# ==========================================

@router.post("/predict")
def predict_crop_yield(
    data: PredictionInput,
    db: Session = Depends(get_db)
):

    # Create DataFrame
    input_df = pd.DataFrame({
        "Area": [data.Area],
        "Item": [data.Item],
        "Year": [data.Year],
        "average_rain_fall_mm_per_year": [
            data.average_rain_fall_mm_per_year
        ],
        "pesticides_tonnes": [
            data.pesticides_tonnes
        ],
        "avg_temp": [
            data.avg_temp
        ]
    })

    # Data Preprocessing
    transformed = preprocessor.transform(
        input_df
    )

    # Prediction
    prediction = model.predict(
        transformed
    )

    prediction_value = round(
        float(prediction[0]),
        2
    )

    # Save Prediction To Database
    save_prediction(
        db=db,
        country=data.Area,
        crop=data.Item,
        year=data.Year,
        rainfall=data.average_rain_fall_mm_per_year,
        pesticides=data.pesticides_tonnes,
        temperature=data.avg_temp,
        predicted_yield=prediction_value
    )

    # API Response
    return {
        "predicted_yield": prediction_value,
        "message": "Prediction Saved Successfully"
    }

# ==========================================
# Get Prediction History
# ==========================================

@router.get("/history")
def get_prediction_history(
    db: Session = Depends(get_db)
):

    predictions = get_predictions(db)

    result = []

    for row in predictions:

        result.append(
            {
                "id": row.id,
                "country": row.country,
                "crop": row.crop,
                "year": row.year,
                "predicted_yield": row.predicted_yield,
                "created_at": row.created_at
            }
        )

    return result