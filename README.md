# FastAPI Secure User App

## Overview
This project is a FastAPI application that implements a secure user model along with a calculation system using SQLAlchemy and Pydantic. It supports user authentication, validation, and PostgreSQL integration, developed across Modules 10, 11, 12 and 13.

---

## Module 10: Secure User Model & CI/CD

### Features
- Secure user model with SQLAlchemy
- Pydantic validation for request and response schemas
- Password hashing and verification
- PostgreSQL database integration
- Unit tests and integration tests
- Docker support
- GitHub Actions CI/CD
- Docker Hub deployment

---

## Module 11: Calculation Model & Factory Pattern

### Features
- Calculation model using SQLAlchemy
- Supports Add, Subtract, Multiply, Divide operations
- Factory pattern for dynamic calculation handling
- Validation for division by zero and invalid types
- Unit testing for calculation logic
- Database storage for calculations

---

## Module 12: API Routes & Integration Testing

### Features
- User registration and login endpoints
- Full CRUD operations for calculations:
  - Create
  - Read (all and by ID)
  - Update
  - Delete
- Integration testing using FastAPI TestClient
- End-to-end backend functionality
- Integration tests validate user registration, login, and calculation CRUD operations
- API tested manually using FastAPI Swagger UI (/docs)
- Proper HTTP status codes used for error handling (400, 404)

---

## Technologies Used
- Python 3.12
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- PostgreSQL
- Passlib (bcrypt)
- Pytest
- Playwright
- Docker
- GitHub Actions

---
## Module 13: JWT Authentication, Frontend & Playwright E2E

### Features
- JWT-based authentication for login and registration
- Token generation on successful login
- Secure password hashing using bcrypt
- Frontend pages:
  - `register.html`
  - `login.html`
- Client-side validation:
  - Email format validation
  - Minimum password length
  - Password confirmation check
- Playwright End-to-End (E2E) testing:
  - Register with valid data
  - Register with short password (error case)
  - Login with correct credentials
  - Login with wrong password (error case)
- CI/CD pipeline updated to include Playwright tests
- Docker image automatically pushed after successful tests

---

## Project Structure
```
fastapi-secure-user-app/
│-- app/
│ │-- api/
│ │ ├── users.py
│ │ ├── calculations.py
│ │ └── auth.py
│ │-- core/
│ │ ├── security.py
│ │ ├── calculation_factory.py
│ │ └── jwt_handler.py
│ │-- models/
│ │ ├── user.py
│ │ └── calculation.py
│ │-- schemas/
│ │ ├── user.py
│ │ ├── calculation.py
│ │ └── auth.py
│ │-- static/
│ │ ├── register.html
│ │ └── login.html
│ │-- database.py
│ │-- main.py
│-- tests/
│ │-- test_security.py
│ │-- test_schemas.py
│ │-- test_users_integration.py
│ │-- test_calculation_unit.py
│ │-- test_calculation_db.py
│ │-- test_calculation_api.py
│ │-- test_e2e.spec.js
│-- .github/workflows/ci.yml
│-- Dockerfile
│-- docker-compose.yml
│-- requirements.txt
│-- pytest.ini
│-- playwright.config.js
│-- README.md
```

---

## Running the Application

### Run with Docker
```bash
docker compose up --build
```

### Open in Browser
- App: http://localhost:8000  
- Swagger Docs: http://localhost:8000/docs  


### Frontend Access
- http://localhost:8000/static/register.html
- http://localhost:8000/static/login.html
---

## Running Tests

### Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run Tests
```bash
pytest -v
```

### Run Playwright
```bash
npx playwright install
npx playwright test
```

### With PostgreSQL
```bash
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/fastapi_db pytest -v
```

---

## API Endpoints

### User Endpoints
- POST `/users/register` → Register user  
- POST `/users/login` → Login user
- Login verifies hashed passwords securely

---

### Calculation Endpoints
- POST `/calculations/` → Create  
- GET `/calculations/` → Get all  
- GET `/calculations/{id}` → Get by ID  
- PUT `/calculations/{id}` → Update  
- DELETE `/calculations/{id}` → Delete  
---

## Calculation Logic
Supports:
- Add
- Subtract
- Multiply
- Divide  

-Uses Factory Pattern for scalability.
Results are computed using a factory method and stored in the database.
---

## Security
- Passwords are hashed before storing
- JWT tokens used for authentication
- Passwords are never returned in API responses
- Username and email are unique
- Email is validated using Pydantic


---

## Continuous Integration & Deployment
GitHub Actions automatically:
- Installs dependencies
- Runs tests
- Runs Playwright E2E tests
- Uses PostgreSQL service
- Builds Docker image

---

## Docker Hub
https://hub.docker.com/r/geethikachowdary/fastapi-secure-user-app

---

## Test Results
```
14 passed, 2 warnings
4 Playwright tests passed
```
## Learning Outcomes
- Backend development with FastAPI
- Database design with SQLAlchemy
- Validation with Pydantic
- Secure authentication
- Factory design pattern
- Secure authentication with JWT
- End-to-End testing with Playwright
- API testing with Pytest
- Docker containerization
- CI/CD with GitHub Actions
---

## Status
- Application working
- All modules implemented (10, 11, 12, 13)
- All tests passing
- CI/CD configured

---

## Reflection
In this project, I worked across multiple modules to build a complete backend system. In Module 10, I learned how to implement secure user authentication with password hashing and validation. In Module 11, I extended the application by adding a calculation system using a factory pattern, which helped me understand scalable design.

In Module 12, I integrated everything by building API routes and performing full CRUD operations with proper testing. I also gained experience using Docker and GitHub Actions for automation. Overall, this project improved my understanding of backend development, testing, and deployment workflows.

In Module 13, I implemented JWT-based authentication and developed frontend pages for user interaction. I also created Playwright tests to validate both successful and error scenarios, ensuring reliability from a user perspective. Additionally, I enhanced the CI/CD pipeline to include full-stack testing and automated Docker deployment. This project improved my understanding of integrating backend, frontend, testing, and deployment into a unified workflow.
