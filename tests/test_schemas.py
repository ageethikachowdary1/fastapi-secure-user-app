from app.schemas.user import UserCreate
import pytest


def test_valid_user_schema():
    user = UserCreate(
        username="testuser",
        email="test@example.com",
        password="mypassword123"
    )

    assert user.username == "testuser"
    assert user.email == "test@example.com"


def test_invalid_email():
    with pytest.raises(Exception):
        UserCreate(
            username="testuser",
            email="invalid-email",
            password="mypassword123"
        )
