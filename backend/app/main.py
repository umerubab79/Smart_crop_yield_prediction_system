from fastapi import FastAPI

from backend.app.routers.prediction_router import router as prediction_router
from backend.app.routers.auth_router import router as auth_router

app = FastAPI(
    title="Smart Crop Yield Prediction API",
    version="1.0.0"
)

app.include_router(prediction_router)

app.include_router(auth_router)