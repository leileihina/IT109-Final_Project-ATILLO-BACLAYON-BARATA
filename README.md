# SkillHub — Student Gig & Skill Marketplace

## Project Overview

SkillHub is a web-based marketplace designed to connect
students who offer freelance services with students and
faculty members who need assistance with projects and tasks.

The system is developed for IT 109 — System Integration
and Architecture.

The current implementation focuses on user authentication,
registration, login, REST API integration, and role-based
access control.

## Technology Stack

### Frontend

- Nuxt 3.21.11
- Vue 3.5.46
- TypeScript
- Tailwind CSS 4.3.5
- Shadcn-Vue
- Shadcn-Nuxt 2.9.0
- Reka UI 2.11.0
- Zod 4.6.7
- Lucide Vue

### Backend

- Python 3.13
- FastAPI
- Uvicorn
- SQLAlchemy ORM
- Pydantic
- PyJWT
- Argon2 Password Hashing
- Psycopg

### Database

- PostgreSQL
- Supabase

### Development Tools

- Visual Studio Code
- Git and GitHub
- Swagger UI
- Node.js and npm

## Current Features

- User registration
- User login
- User logout
- Username and password regex validation
- Frontend and backend input validation
- Secure password hashing using Argon2
- JWT-based authentication
- Role-based access control (RBAC)
- Protected frontend routes
- Protected backend API endpoints
- Role-specific dashboards
- PostgreSQL database integration
- REST API request and response handling

## User Roles

### Client

Clients are students or faculty members who need
freelance services.

Planned marketplace functionalities:

- Post project requests
- Browse freelancers
- Hire freelancers
- Manage project requests

### Freelancer

Freelancers are students who offer their skills
and services.

Planned marketplace functionalities:

- Offer freelance services
- Browse available projects
- Apply for projects
- Manage service listings

### Admin

Administrators are responsible for managing and
monitoring the platform.

Planned marketplace functionalities:

- Manage users
- Approve listings
- Oversee transactions

Public registration is limited to Client and
Freelancer accounts. Administrator accounts are
created separately through a backend script.

## System Architecture

The system follows a client-server architecture.

Nuxt Frontend
      |
      | HTTP Requests / JSON Responses
      v
FastAPI REST API
      |
      | SQLAlchemy ORM
      v
PostgreSQL (Supabase)

The frontend communicates with the backend through
REST API endpoints. The backend processes requests,
validates user input, handles authentication, and
communicates with the database.

## Project Structure

```text
student-gig-marketplace/
├── backend/
│   ├── app/
│   │   ├── routers/
│   │   │   ├── auth.py
│   │   │   └── dashboard.py
│   │   ├── database.py
│   │   ├── dependencies.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── security.py
│   ├── .env.example
│   ├── create_admin.py
│   ├── init_db.py
│   └── requirements.txt
├── frontend/
│   ├── assets/
│   ├── components/
│   ├── composables/
│   ├── layouts/
│   ├── lib/
│   ├── middleware/
│   ├── pages/
│   ├── public/
│   ├── types/
│   ├── .env.example
│   ├── app.vue
│   ├── components.json
│   ├── nuxt.config.ts
│   ├── package.json
│   └── package-lock.json
├── .gitignore
└── README.md
```

## Installation and Setup

### Prerequisites

Make sure the following tools are installed:

- Node.js 24
- npm
- Python 3.13
- Git
- Visual Studio Code
- A Supabase account and PostgreSQL database

### 1. Clone the Repository

```bash
git clone https://github.com/leileihina/IT109-Final_Project-ATILLO-BACLAYON-BARATA.git
cd student-gig-marketplace
```

### 2. Backend Setup

Navigate to the backend directory.

```powershell
cd backend
```

Create a Python virtual environment.

```powershell
python -m venv .venv
```

Activate the virtual environment on Windows.

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required dependencies.

```powershell
python -m pip install -r requirements.txt
```

### 3. Configure Backend Environment Variables

Create a copy of the environment template.

```powershell
Copy-Item .env.example .env
```

Configure the following variables inside backend/.env.

```env
DATABASE_URL="YOUR_POSTGRESQL_CONNECTION_STRING"
JWT_SECRET_KEY="YOUR_SECRET_KEY"
JWT_ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

Use the PostgreSQL connection string from Supabase.
For IPv4 compatibility, use the Session Pooler
connection string with the SQLAlchemy psycopg driver.

Example connection string format:

```env
DATABASE_URL="postgresql+psycopg://USERNAME:PASSWORD@HOST:5432/postgres?sslmode=require"
```

Generate a JWT secret key using:

```powershell
python -c "import secrets; print(secrets.token_hex(32))"
```

Never upload actual database credentials or secret
keys to GitHub.

### 4. Initialize the Database

Run the following command:

```powershell
python init_db.py
```

This creates the required users table in PostgreSQL.

In the Supabase SQL Editor, execute:

```sql
ALTER TABLE public.users ENABLE ROW LEVEL SECURITY;

REVOKE ALL ON TABLE public.users
FROM anon, authenticated;
```

These settings restrict direct access to the users
table through Supabase's public API roles.

### 5. Create an Administrator Account

Run:

```powershell
python create_admin.py
```

Follow the instructions displayed in the terminal
to configure the administrator password.

### 6. Run the Backend

```powershell
python -m uvicorn app.main:app --reload
```

The backend will be available at:

http://127.0.0.1:8000

Swagger API documentation:

http://127.0.0.1:8000/docs

### 7. Frontend Setup

Open a separate terminal from the project root.

```powershell
cd frontend
```

Install the required frontend dependencies.

```powershell
npm ci
```

Create the frontend environment file.

```powershell
Copy-Item .env.example .env
```

Configure the API base URL inside frontend/.env.

```env
NUXT_PUBLIC_API_BASE=http://127.0.0.1:8000
```

Run the frontend development server.

```powershell
npm run dev
```

Open the application in your browser:

http://localhost:3000

Both frontend and backend servers must be running
for the application to function correctly.

## API Endpoints

### General Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Backend welcome message |
| GET | /api/health | Backend health check |

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/auth/register | Register a new user |
| POST | /api/auth/login | Authenticate a user |
| GET | /api/auth/me | Retrieve authenticated user information |

### Protected Dashboard Endpoints

| Method | Endpoint | Required Role |
|--------|----------|---------------|
| GET | /api/dashboard/client | Client |
| GET | /api/dashboard/freelancer | Freelancer |
| GET | /api/dashboard/admin | Admin |

Protected endpoints require a valid JWT access token.

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## Authentication Process

### Registration

1. The user completes the registration form.
2. The frontend validates the submitted information.
3. The frontend sends a POST request to the backend.
4. The backend validates the submitted information.
5. The password is hashed using Argon2.
6. The user account is stored in PostgreSQL.
7. The backend returns a registration response.

### Login

1. The user enters a username and password.
2. The frontend validates the login form.
3. The frontend sends a login request to FastAPI.
4. The backend verifies the user's credentials.
5. The backend generates a JWT access token.
6. The frontend receives the token and user information.
7. The user is redirected to the appropriate dashboard.

### Logout

1. The frontend clears the stored authentication state.
2. The user is redirected to the login page.
3. Protected frontend routes require authentication again.

Previously issued JWTs remain valid until expiration
unless additional token revocation is implemented.

## Input Validation

Username and password validation are implemented
on both the frontend and backend.

### Username Requirements

- Minimum of 4 characters
- Maximum of 20 characters
- Letters, numbers, and underscores only
- No spaces or other special characters

Regular expression:

```regex
^[a-zA-Z0-9_]{4,20}$
```

### Password Requirements

- Minimum of 8 characters
- Maximum of 128 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- At least one special character from !@#$%^&*

Regular expression:

```regex
^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*]).{8,128}$
```

## Role-Based Access Control

The system restricts dashboard access based on
the authenticated user's assigned role.

| User Role | Client Dashboard | Freelancer Dashboard | Admin Dashboard |
|-----------|------------------|----------------------|-----------------|
| Client | Allowed | Denied | Denied |
| Freelancer | Denied | Allowed | Denied |
| Admin | Denied | Denied | Allowed |
| Guest | Denied | Denied | Denied |

Frontend middleware protects dashboard pages.

Backend authentication dependencies independently
verify JWT tokens and user roles before granting
access to protected API endpoints.

## Security Features

- Argon2 password hashing
- JWT authentication with token expiration
- Frontend and backend regex validation
- Role-based authorization
- Protected API endpoints
- Protected frontend routes
- Unique username and email constraints
- SQLAlchemy ORM database operations
- Environment variable protection
- Restricted CORS configuration
- Restricted public access to the users table

## Testing

The following functionalities have been tested:

- Valid user registration
- Invalid registration input
- Duplicate username and email handling
- Valid login credentials
- Invalid login credentials
- Client dashboard access
- Freelancer dashboard access
- Admin dashboard access
- Unauthorized role access
- Unauthenticated dashboard access
- Logout functionality
- Frontend and backend API integration
- Database connectivity
- Nuxt production build

## Production Build

To build the frontend for production:

```powershell
cd frontend
npm run build
```

To preview the production build:

```powershell
node .output/server/index.mjs
```

## Current Limitations

This version focuses on authentication and REST API
integration for the current course activity.

- Authentication state is stored in memory.
- Refreshing the page requires the user to log in again.
- Server-side JWT revocation is not yet implemented.
- Google OAuth authentication is not yet implemented.
- CAPTCHA and rate limiting are not yet implemented.
- Marketplace dashboard features are placeholders.
- Payment and other third-party integrations are
  reserved for future development.

This version is intended for local development
and academic demonstration.

## Future Enhancements

- Google OAuth 2.0 authentication
- Persistent authentication sessions
- CAPTCHA and rate limiting
- Project and service listing management
- Freelancer applications
- Client and freelancer transactions
- Payment integration
- Email notifications
- Caching
- Object storage

## Course Information

Course: IT 109 — System Integration and Architecture

Project: Student Gig & Skill Marketplace

System Name: SkillHub

Institution: Caraga State University

## Development Team

- Sheina Atillo
- Rubbie Jane Baclayon
- Eleanore Barata

## Project Status

Authentication and REST API Integration — Completed

Full Marketplace Implementation — In Development

## Acknowledgment

This project is developed for academic purposes as
part of the requirements for IT 109 — System
Integration and Architecture.