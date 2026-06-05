from fastapi import FastAPI

from backend.app.database.connection import engine
from backend.app.database.models import Base

from backend.app.routers.prediction_router import router as prediction_router
from backend.app.routers.auth_router import router as auth_router

# ==========================================
# Create Database Tables
# ==========================================

Base.metadata.create_all(bind=engine)

# ==========================================
# FastAPI App
# ==========================================

app = FastAPI(
    title="Smart Crop Yield Prediction API",
    version="1.0.0"
)

# ==========================================
# Routers
# ==========================================

app.include_router(prediction_router)

app.include_router(auth_router)


# ==========================================
# Root Endpoint
# ==========================================

@app.get("/")
def root():
    return {
        "message": "Smart Crop Yield Prediction API Running Successfully"
    }