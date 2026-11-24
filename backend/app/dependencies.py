from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from jwt.exceptions import InvalidTokenError

from app.database import get_db
from app.models import User
from app.security import decode_access_token


# Extract the Bearer token from the request
bearer_scheme = HTTPBearer(auto_error=False)


# Retrieve the currently authenticated user
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db)
):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired authentication token.",
        headers={"WWW-Authenticate": "Bearer"}
    )

    # Check if a token was provided
    if credentials is None:
        raise credentials_exception

    try:
        # Decode and verify the token
        payload = decode_access_token(
            credentials.credentials
        )

        user_id = int(payload["sub"])

    except (InvalidTokenError, ValueError, TypeError, KeyError):
        raise credentials_exception

    # Retrieve the user from the database
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        raise credentials_exception

    # Check account status
    if not user.is_active:
        raise HTTPException(
            status_code=403,
            detail="Account is inactive."
        )

    return user


# Restrict access based on user roles
def require_role(*allowed_roles: str):

    def role_checker(
        current_user: User = Depends(get_current_user)
    ):

        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=403,
                detail="You do not have permission to access this resource."
            )

        return current_user

    return role_checker