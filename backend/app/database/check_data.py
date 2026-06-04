# ==========================================
# Check Saved Predictions
# ==========================================

from backend.app.database.connection import SessionLocal
from backend.app.database.models import PredictionHistory

db = SessionLocal()

predictions = db.query(
    PredictionHistory
).all()

print("\n===== SAVED PREDICTIONS =====\n")

for row in predictions:
    print(
        row.id,
        row.country,
        row.crop,
        row.predicted_yield
    )

db.close()