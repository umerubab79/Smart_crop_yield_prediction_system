# ==========================================
# Database Connection Configuration
# ==========================================

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ==========================================
# SQLite Database
# ==========================================

# Render aur local dono par work karega
DATABASE_URL = "sqlite:///./crop_prediction.db"

# ==========================================
# Create Engine
# ==========================================

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# ==========================================
# Session Factory
# ==========================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ==========================================
# Base Model
# ==========================================

Base = declarative_base()

# ==========================================
# Database Dependency
# ==========================================

def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()