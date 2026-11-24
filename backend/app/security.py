import os
import jwt

from datetime import datetime, timedelta, timezone
from pathlib import Path
from dotenv import load_dotenv
from pwdlib import PasswordHash


# Load environment variables
load_dotenv(Path(__file__).resolve().parent.parent / ".env")


# JWT configuration
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60")
)

if not SECRET_KEY:
    raise ValueError("JWT_SECRET_KEY is not configured.")


# Initialize password hashing
password_hash = PasswordHash.recommended()


# Hash a plain-text password
def hash_password(password: str) -> str:
    return password_hash.hash(password)


# Verify a password
def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:

    return password_hash.verify(
        plain_password,
        hashed_password
    )


# Generate a JWT access token
def create_access_token(data: dict) -> str:

    token_data = data.copy()

    expiration = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    token_data.update({"exp": expiration})

    encoded_jwt = jwt.encode(
        token_data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt

# Decode and verify a JWT access token
def decode_access_token(token: str) -> dict:

    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM],
        options={"require": ["exp", "sub"]}
    )

    return payload