import re

from getpass import getpass
from app.database import SessionLocal
from app.models import User
from app.security import hash_password


def create_admin():

    db = SessionLocal()

    try:
        # Check if the admin account already exists
        existing_admin = db.query(User).filter(
            User.username == "admin"
        ).first()

        if existing_admin:
            print("Admin account already exists.")
            return

        # Enter password securely
        password = getpass("Enter admin password: ")
        confirm_password = getpass("Confirm admin password: ")

        # Check if passwords match
        if password != confirm_password:
            print("Passwords do not match.")
            return

        # Validate password using regex
        pattern = (
            r"^(?=.*[a-z])"
            r"(?=.*[A-Z])"
            r"(?=.*[0-9])"
            r"(?=.*[!@#$%^&*]).{8,128}$"
        )

        if not re.fullmatch(pattern, password):
            print("Password does not meet the requirements.")
            return

        # Create the administrator account
        admin = User(
            first_name="System",
            last_name="Administrator",
            username="admin",
            email="admin@example.com",
            hashed_password=hash_password(password),
            role="admin",
            is_active=True
        )

        db.add(admin)
        db.commit()

        print("Admin account created successfully!")

    except Exception:
        db.rollback()
        print("Failed to create admin account.")
        raise

    finally:
        db.close()


if __name__ == "__main__":
    create_admin()