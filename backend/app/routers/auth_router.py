from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from backend.app.database.connection import get_db
from backend.app.database.crud import create_user
from backend.app.database.crud import get_user_by_username
from backend.app.database.crud import get_user_by_email
from backend.app.database.crud import login_user

from backend.app.schemas.user_schema import UserRegister
from backend.app.schemas.user_schema import UserLogin

router = APIRouter()


# ==========================================
# Register
# ==========================================

@router.post("/register")
def register_user(
    user: UserRegister,
    db: Session = Depends(get_db)
):

    existing_username = get_user_by_username(
        db,
        user.username
    )

    if existing_username:

        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    existing_email = get_user_by_email(
        db,
        user.email
    )

    if existing_email:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    create_user(
        db=db,
        full_name=user.full_name,
        username=user.username,
        email=user.email,
        password=user.password
    )

    return {
        "message": "User Registered Successfully"
    }


# ==========================================
# Login
# ==========================================

@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    existing_user = login_user(
        db,
        user.username,
        user.password
    )

    if not existing_user:

        raise HTTPException(
            status_code=401,
            detail="Invalid Username or Password"
        )

    return {
        "message": "Login Successful",
        "username": existing_user.username
    }