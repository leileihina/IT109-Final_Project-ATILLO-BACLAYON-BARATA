from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database import get_db
from app.models import User
from app.schemas import (
    UserRegister,
    UserResponse,
    UserLogin,
    TokenResponse
)

from app.security import (
    hash_password,
    verify_password,
    create_access_token
)


router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(user: UserRegister, db: Session = Depends(get_db)):

    # Normalize username and email
    username = user.username.lower()
    email = user.email.lower()

    # Check if username already exists
    existing_username = db.query(User).filter(
        User.username == username
    ).first()

    if existing_username:
        raise HTTPException(
            status_code=409,
            detail="Username is already registered."
        )

    # Check if email already exists
    existing_email = db.query(User).filter(
        User.email == email
    ).first()

    if existing_email:
        raise HTTPException(
            status_code=409,
            detail="Email is already registered."
        )

    # Create a new user with a hashed password
    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        username=username,
        email=email,
        hashed_password=hash_password(user.password),
        role=user.role,
        is_active=True
    )

    # Save the user to the database
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=409,
            detail="Username or email is already registered."
        )

    # Return the registered user without the password
    return new_user

@router.post(
    "/login",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK
)
def login(user: UserLogin, db: Session = Depends(get_db)):

    # Find the registered user
    existing_user = db.query(User).filter(
        User.username == user.username.lower()
    ).first()

    # Check if the username and password are correct
    if not existing_user or not verify_password(
        user.password,
        existing_user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password."
        )

    # Check if the account is active
    if not existing_user.is_active:
        raise HTTPException(
            status_code=403,
            detail="Account is inactive."
        )

    # Generate JWT access token
    access_token = create_access_token(
        data={
            "sub": str(existing_user.id),
            "role": existing_user.role
        }
    )

    # Return the token and user information
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": existing_user
    }
    
from app.dependencies import get_current_user

@router.get(
    "/me",
    response_model=UserResponse
)
def get_me(
    current_user: User = Depends(get_current_user)
):

    return current_user