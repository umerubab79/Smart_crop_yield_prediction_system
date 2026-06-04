# ==========================================
# Create Database Tables
# ==========================================

from backend.app.database.connection import engine
from backend.app.database.connection import Base

# Import Models
from backend.app.database.models import PredictionHistory
from backend.app.database.models import User

Base.metadata.create_all(bind=engine)

print("Tables Created Successfully")