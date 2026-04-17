from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)


def test_create_user_success():
    unique_id = uuid.uuid4().hex[:8]
    username = f"integration_user_{unique_id}"
    email = f"integration_{unique_id}@example.com"

    response = client.post(
        "/users/register",
        json={
            "username": username,
            "email": email,
            "password": "mypassword123"
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert data["username"] == username
    assert data["email"] == email


def test_duplicate_user():
    unique_id = uuid.uuid4().hex[:8]
    username = f"duplicate_user_{unique_id}"
    email = f"duplicate_{unique_id}@example.com"

    first_response = client.post(
        "/users/register",
        json={
            "username": username,
            "email": email,
            "password": "mypassword123"
        }
    )

    assert first_response.status_code == 200

    response = client.post(
        "/users/register",
        json={
            "username": username,
            "email": email,
            "password": "mypassword123"
        }
    )

    assert response.status_code == 400
