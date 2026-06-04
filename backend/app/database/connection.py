# ==========================================
# Database Connection Configuration
# ==========================================

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite Database Path
DATABASE_URL = "sqlite:///./database/crop_prediction.db"

# Create Database Engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Database Session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base Class For Models
Base = declarative_base()


# Dependency Function
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()