import re

from datetime import datetime
from typing import Literal
from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    ConfigDict,
    field_validator
)


# Registration request schema
class UserRegister(BaseModel):

    first_name: str = Field(
        min_length=1,
        max_length=100
    )

    last_name: str = Field(
        min_length=1,
        max_length=100
    )

    username: str = Field(
        min_length=4,
        max_length=20,
        pattern=r"^[a-zA-Z0-9_]+$"
    )

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=128
    )

    role: Literal["client", "freelancer"]

    # Password regex validation
    @field_validator("password")
    @classmethod
    def validate_password(cls, password: str):

        pattern = (
            r"^(?=.*[a-z])"
            r"(?=.*[A-Z])"
            r"(?=.*[0-9])"
            r"(?=.*[!@#$%^&*]).{8,128}$"
        )

        if not re.fullmatch(pattern, password):
            raise ValueError(
                "Password must contain an uppercase letter, "
                "a lowercase letter, a number, "
                "and a special character (!@#$%^&*)."
            )

        return password


# User response schema
class UserResponse(BaseModel):

    id: int
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    role: str
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
    
# Login request schema
class UserLogin(BaseModel):

    username: str = Field(
        min_length=4,
        max_length=20,
        pattern=r"^[a-zA-Z0-9_]+$"
    )

    password: str = Field(
        min_length=1,
        max_length=128
    )


# Login response schema
class TokenResponse(BaseModel):

    access_token: str
    token_type: str = "bearer"
    user: UserResponse