from app.core.security import hash_password, verify_password


def test_hash_password():
    password = "mypassword123"
    hashed = hash_password(password)

    assert hashed != password
    assert verify_password(password, hashed) is True


def test_verify_password_wrong():
    password = "mypassword123"
    hashed = hash_password(password)

    assert verify_password("wrongpassword", hashed) is False
