# FastAPI Secure User App

## Overview
This project is a FastAPI application that implements a secure user model using SQLAlchemy and Pydantic. It supports user creation with password hashing, validation, and PostgreSQL integration.

---

## Features
- Secure user model with SQLAlchemy
- Pydantic validation for request and response schemas
- Password hashing and verification
- PostgreSQL database integration
- Unit tests and integration tests
- Docker support
- GitHub Actions CI/CD
- Docker Hub deployment

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
- Docker
- GitHub Actions

---

## Project Structure
fastapi-secure-user-app/
│-- app/
│   │-- api/
│   │   └── users.py
│   │-- core/
│   │   └── security.py
│   │-- models/
│   │   └── user.py
│   │-- schemas/
│   │   └── user.py
│   │-- database.py
│   │-- main.py
│-- tests/
│   │-- test_security.py
│   │-- test_schemas.py
│   │-- test_users_integration.py
│-- .github/
│   │-- workflows/
│   │   └── ci.yml
│-- Dockerfile
│-- docker-compose.yml
│-- requirements.txt
│-- pytest.ini
│-- README.md

---

## Running the Application

### Run with Docker
```bash
docker compose up --build
```

### Open in Browser
App: http://localhost:8000  
Swagger Docs: http://localhost:8000/docs

---

## Running Tests

### Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run Tests
```bash
pytest -v
```

### Run Tests with PostgreSQL
```bash
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/fastapi_db pytest -v
```

---

## Security
- Passwords are hashed before storing
- Passwords are never returned in API responses
- Username and email are unique
- Email is validated using Pydantic

---

## Continuous Integration
GitHub Actions automatically:
- Installs dependencies
- Runs tests
- Starts PostgreSQL service
- Builds Docker image
- Pushes Docker image to Docker Hub

---

## Docker Hub
https://hub.docker.com/r/geethikachowdary/fastapi-secure-user-app

---

## Learning Outcomes
- REST API development using FastAPI
- SQLAlchemy model design
- Pydantic validation
- Password hashing and security
- PostgreSQL integration
- Unit and integration testing
- Docker containerization
- CI/CD using GitHub Actions

---

## Status
- Application working
- User creation working
- Validation working
- All tests passing
- CI/CD configured

---

## Reflection
During this assignment, I learned how to build a secure backend application using FastAPI, SQLAlchemy, and Pydantic. I understood how to properly validate user input and securely store passwords using hashing.

I also gained experience with PostgreSQL, Docker, and GitHub Actions. Setting up CI/CD helped me understand how real-world applications are tested and deployed automatically. This project improved my understanding of backend development, testing, and deployment workflows.

#Module12
## API Endpoints

### User Endpoints
- POST /users → Create a new user

Example:
```json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "mypassword"
}

##Root Endpoint
GET / → Check if application is running


👉 Shows you understand API design

---

# 🔥 2. Add Calculation Explanation (IMPORTANT FOR MODULE 11)

```md
## Calculation Logic

The application supports four types of operations:
- Add
- Subtract
- Multiply
- Divide

A factory pattern is used to dynamically select the correct operation. This makes the system scalable and easy to extend for future operations.

Example:
- Add → a + b
- Divide → a / b (with validation for zero division)


## Validation and Error Handling

- Invalid email formats are rejected using Pydantic
- Duplicate username/email is not allowed
- Division by zero is prevented
- Invalid calculation types raise errors

## Test Results

All tests passed successfully:

13 passed, 1 warning


