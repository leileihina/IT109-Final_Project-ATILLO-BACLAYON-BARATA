from fastapi import APIRouter, Depends

from app.models import User
from app.dependencies import require_role


router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"]
)


# Client dashboard
@router.get("/client")
def client_dashboard(
    current_user: User = Depends(require_role("client"))
):
    return {
        "message": "Welcome to the Client Dashboard!",
        "username": current_user.username,
        "role": current_user.role,
        "permissions": [
            "Post project requests",
            "Browse freelancers",
            "Hire freelancers"
        ]
    }


# Freelancer dashboard
@router.get("/freelancer")
def freelancer_dashboard(
    current_user: User = Depends(require_role("freelancer"))
):
    return {
        "message": "Welcome to the Freelancer Dashboard!",
        "username": current_user.username,
        "role": current_user.role,
        "permissions": [
            "Offer services",
            "Browse available projects",
            "Apply for projects"
        ]
    }


# Admin dashboard
@router.get("/admin")
def admin_dashboard(
    current_user: User = Depends(require_role("admin"))
):
    return {
        "message": "Welcome to the Admin Dashboard!",
        "username": current_user.username,
        "role": current_user.role,
        "permissions": [
            "Manage users",
            "Approve listings",
            "Oversee transactions"
        ]
    }