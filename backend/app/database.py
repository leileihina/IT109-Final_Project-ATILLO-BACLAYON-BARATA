import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Load environment variables from the backend .env file
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

# Retrieve the database connection string
DATABASE_URL = os.getenv("DATABASE_URL")

# Check if the database URL exists
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not configured.")

# Create the database engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

# Create a database session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for database models
class Base(DeclarativeBase):
    pass

# Provide a database session to API endpoints
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()