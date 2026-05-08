# FastAPI Secure User App

## Overview
This project is a secure FastAPI web application developed across multiple modules and finalized as a complete full-stack application.

The application includes:
- Secure user registration and authentication
- JWT-based login security
- Calculation management with full BREAD functionality
- Advanced reporting dashboard for calculation analytics
- Automated backend and frontend testing
- Docker containerization
- GitHub Actions CI/CD pipeline
- Docker Hub deployment

---

## Module 10: Secure User Model & CI/CD

### Features
- Secure user model using SQLAlchemy
- Pydantic schemas for validation
- Password hashing and verification
- PostgreSQL database integration
- Unit tests and integration tests
- Docker support
- GitHub Actions CI/CD setup
- Docker Hub deployment

---

## Module 11: Calculation Model & Factory Pattern

### Features
- Calculation model using SQLAlchemy
- Supports:
  - Add
  - Subtract
  - Multiply
  - Divide
- Factory pattern for dynamic operation handling
- Division-by-zero validation
- Unit testing for calculation logic
- Database persistence for calculations

---

## Module 12: API Routes & Integration Testing

### Features
- User registration API
- User login API
- Full CRUD backend endpoints for calculations
- FastAPI TestClient integration testing
- API testing through Swagger UI
- Proper HTTP response handling
- Backend validation and error handling

---

## Module 13: JWT Authentication, Frontend & Playwright E2E

### Features
- JWT-based authentication
- Secure login token generation
- Password hashing using bcrypt
- Frontend user pages:
  - register.html
  - login.html
- Client-side validation:
  - Email validation
  - Password confirmation
  - Minimum password checks
- Playwright E2E tests:
  - Valid registration
  - Invalid registration
  - Successful login
  - Invalid login
- CI/CD pipeline updated with Playwright automation
- Docker deployment after successful tests

---

## Module 14: Complete BREAD Functionality for Calculations

### Features
- Frontend calculation dashboard
- Browse calculations
- Read calculation by ID
- Add new calculations
- Edit existing calculations
- Delete calculations
- Client-side numeric validation
- Divide-by-zero frontend validation
- Playwright E2E calculation workflow testing
- GitHub Actions automated testing
- Docker image deployment

### Frontend Page
http://localhost:8000/static/calculations.html

### Calculation Endpoints
- GET `/calculations/` → Browse
- GET `/calculations/{id}` → Read
- POST `/calculations/` → Add
- PUT `/calculations/{id}` → Edit
- DELETE `/calculations/{id}` → Delete

---

## Final Project: Advanced Feature Integration (Calculation Report Dashboard)

### Features
- Advanced reporting dashboard
- Total calculations count
- Operation usage statistics
- Average result
- Highest result
- Lowest result
- Recent calculations summary
- Frontend dashboard integration
- Report API endpoint
- Backend integration testing
- Playwright end-to-end report testing
- Docker deployment support
- CI/CD integration

### New Files Added
Backend:
- `app/api/reports.py`
- `app/schemas/report.py`

Frontend:
- `app/static/report.html`

Testing:
- `tests/test_report_api.py`

### Report API Endpoint
- GET `/reports/calculations`

### Report Dashboard
http://localhost:8000/static/report.html

### Final Project Test Results
```text
15 backend tests passed
7 Playwright tests passed
GitHub Actions workflow passed successfully
Docker deployment successful
```

### Final Project Reflection
For the final project, I extended the secure FastAPI calculator application by implementing an advanced Calculation Report Dashboard feature.

This feature provides analytics such as total calculations, operation frequency, average results, highest and lowest values, and recent calculation history.

To implement this, I developed backend report APIs, database queries, frontend dashboard integration, API tests, and Playwright end-to-end testing.

This final project strengthened my understanding of FastAPI backend development, PostgreSQL integration, frontend-backend communication, automated testing, Docker deployment, and CI/CD workflows.

---

## Technologies Used
- Python 3.12
- FastAPI
- Uvicorn
- SQLAlchemy
- PostgreSQL
- Pydantic
- Passlib (bcrypt)
- JWT
- Pytest
- Playwright
- Docker
- Docker Compose
- GitHub Actions

---

## Project Structure

```text
fastapi-secure-user-app/
│
├── app/
│   ├── api/
│   │   ├── users.py
│   │   ├── calculations.py
│   │   ├── auth.py
│   │   └── reports.py
│   │
│   ├── core/
│   │   ├── security.py
│   │   ├── calculation_factory.py
│   │   └── jwt_handler.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── calculation.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── calculation.py
│   │   ├── auth.py
│   │   └── report.py
│   │
│   ├── static/
│   │   ├── register.html
│   │   ├── login.html
│   │   ├── calculations.html
│   │   └── report.html
│   │
│   ├── database.py
│   └── main.py
│
├── tests/
│   ├── test_security.py
│   ├── test_schemas.py
│   ├── test_users_integration.py
│   ├── test_calculation_unit.py
│   ├── test_calculation_db.py
│   ├── test_calculation_api.py
│   ├── test_report_api.py
│   └── test_e2e.spec.js
│
├── .github/workflows/ci.yml
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pytest.ini
├── playwright.config.js
└── README.md
```

---

## Running the Application

### Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run with Docker
```bash
docker compose up --build
```

### Run Locally
```bash
uvicorn app.main:app --reload
```

---

## Open in Browser

Application:
http://localhost:8000

Swagger Docs:
http://localhost:8000/docs

Frontend Pages:
- http://localhost:8000/static/register.html
- http://localhost:8000/static/login.html
- http://localhost:8000/static/calculations.html
- http://localhost:8000/static/report.html

---

## Running Tests

Backend:
```bash
export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/fastapi_db
pytest -v
```

Frontend:
```bash
npx playwright test
```

Expected:
```text
15 backend tests passed
7 Playwright tests passed
```

---

## Security
- Password hashing using bcrypt
- JWT authentication
- Pydantic validation
- Duplicate user protection
- Secure API structure
- Division-by-zero prevention

---

## Continuous Integration & Deployment
GitHub Actions automatically:
- Installs dependencies
- Starts PostgreSQL service
- Runs backend tests
- Runs Playwright E2E tests
- Builds Docker image
- Pushes Docker image to Docker Hub

---

## Docker Hub
https://hub.docker.com/r/geethikachowdary/fastapi-secure-user-app

## GitHub Repository
https://github.com/ageethikachowdary1/fastapi-secure-user-app

---

## Learning Outcomes
- Backend development with FastAPI
- Database integration with PostgreSQL
- SQLAlchemy ORM usage
- Secure authentication with JWT
- Frontend-backend integration
- REST API design
- Automated backend testing
- Playwright E2E frontend testing
- Docker containerization
- CI/CD automation
- Full-stack application development

---

## Status
- Application working successfully
- Modules 10, 11, 12, 13, 14 completed
- Final project advanced feature completed
- Backend tests passing
- Frontend tests passing
- Docker deployment working
- GitHub Actions CI/CD working
- Docker Hub deployment working

---

## Final Project Completion Status
 User registration working  
 Secure login with JWT working  
 Full BREAD calculation operations working  
 Advanced reporting dashboard working  
 Report API endpoint working  
 API tests passing  
 Pytest backend tests passing (15 passed)  
 Playwright frontend tests passing (7 passed)  
 Docker deployment working  
 GitHub Actions CI/CD working  
 Docker Hub deployment working  
 Final project completed successfully

---

## Reflection

Throughout this project, I progressively built a complete secure FastAPI web application across multiple modules.

In Module 10, I learned how to create a secure user model using SQLAlchemy and Pydantic, implement password hashing, connect the application with PostgreSQL, and configure Docker along with GitHub Actions CI/CD automation.

In Module 11, I extended the application by adding a calculation system using the factory design pattern. This helped me understand reusable application design, database persistence, validation logic, and backend unit testing.

In Module 12, I implemented API routes for user authentication and calculation management, along with integration testing using FastAPI TestClient. This improved my understanding of REST API development, HTTP status handling, and backend testing workflows.

In Module 13, I added JWT-based authentication and frontend login and registration pages with client-side validation. I also learned how to use Playwright for end-to-end testing and integrate frontend testing into the CI/CD pipeline.

In Module 14, I completed full BREAD functionality for calculations by developing the frontend calculation dashboard and connecting it with backend APIs. This improved my understanding of frontend-backend communication, CRUD workflows, validation, and automated browser testing.

For the final project, I implemented an advanced Calculation Report Dashboard feature. This involved creating new backend APIs, database analytics queries, frontend dashboard integration, API testing, and end-to-end report testing.

Overall, this project significantly improved my practical understanding of FastAPI development, secure authentication, PostgreSQL integration, REST API design, frontend integration, automated testing, Docker deployment, and DevOps workflows.
