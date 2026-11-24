from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth, dashboard


# Initialize the FastAPI application
app = FastAPI(
    title="Student Gig & Skill Marketplace API",
    description="Backend REST API for the Student Gig & Skill Marketplace",
    version="1.0.0"
)


# Allow the Nuxt frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include API routers
app.include_router(auth.router)
app.include_router(dashboard.router)


# Root endpoint
@app.get("/")
def root():
    return {
        "message": "Welcome to the Student Gig & Skill Marketplace API",
        "status": "success"
    }


# Health check endpoint
@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Student Gig Marketplace Backend"
    }