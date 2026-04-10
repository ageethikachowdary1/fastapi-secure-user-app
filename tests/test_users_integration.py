from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_user_success():
    response = client.post(
        "/users",
        json={
            "username": "integration_user",
            "email": "integration@example.com",
            "password": "mypassword123"
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "integration_user"
    assert data["email"] == "integration@example.com"


def test_duplicate_user():
    client.post(
        "/users",
        json={
            "username": "duplicate_user",
            "email": "duplicate@example.com",
            "password": "mypassword123"
        }
    )

    response = client.post(
        "/users",
        json={
            "username": "duplicate_user",
            "email": "duplicate@example.com",
            "password": "mypassword123"
        }
    )

    assert response.status_code == 400
