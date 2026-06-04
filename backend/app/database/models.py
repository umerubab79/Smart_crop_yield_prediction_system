# ==========================================
# Database Models
# ==========================================

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime

from datetime import datetime

from backend.app.database.connection import Base


# ==========================================
# Prediction History Table
# ==========================================

class PredictionHistory(Base):

    __tablename__ = "prediction_history"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)

    # User Inputs
    country = Column(String, nullable=False)

    crop = Column(String, nullable=False)

    year = Column(Integer, nullable=False)

    rainfall = Column(Float, nullable=False)

    pesticides = Column(Float, nullable=False)

    temperature = Column(Float, nullable=False)

    # Model Output
    predicted_yield = Column(Float, nullable=False)

    # Timestamp
    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
# ==========================================
# User Table
# ==========================================

class User(Base):

    __tablename__ = "users"

    # Primary Key
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    full_name = Column(
        String,
        nullable=False
    )

    username = Column(
        String,
        unique=True,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        nullable=False
    )

    password = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )      