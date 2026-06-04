# ==========================================
# Database CRUD Operations
# ==========================================

from sqlalchemy.orm import Session

from backend.app.database.models import PredictionHistory
from backend.app.database.models import User


# ==========================================
# Prediction Operations
# ==========================================

def save_prediction(
    db: Session,
    country,
    crop,
    year,
    rainfall,
    pesticides,
    temperature,
    predicted_yield
):

    prediction = PredictionHistory(
        country=country,
        crop=crop,
        year=year,
        rainfall=rainfall,
        pesticides=pesticides,
        temperature=temperature,
        predicted_yield=predicted_yield
    )

    db.add(prediction)

    db.commit()

    db.refresh(prediction)

    return prediction


def get_predictions(db: Session):

    return db.query(
        PredictionHistory
    ).all()


# ==========================================
# User Operations
# ==========================================

def create_user(
    db: Session,
    full_name,
    username,
    email,
    password
):

    user = User(
        full_name=full_name,
        username=username,
        email=email,
        password=password
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user


def get_user_by_username(
    db: Session,
    username
):

    return (
        db.query(User)
        .filter(User.username == username)
        .first()
    )


def get_user_by_email(
    db: Session,
    email
):

    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )


def login_user(
    db: Session,
    username,
    password
):

    return (
        db.query(User)
        .filter(
            User.username == username,
            User.password == password
        )
        .first()
    )