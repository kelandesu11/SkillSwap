from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_register():
    response = client.post(
        "/api/v1/auth/register",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123",
        },
    )

    assert response.status_code in [201, 400]


def test_login():
    client.post(
        "/api/v1/auth/register",
        json={
            "username": "loginuser",
            "email": "login@example.com",
            "password": "password123",
        },
    )

    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "login@example.com",
            "password": "password123",
        },
    )

    assert response.status_code == 200
    assert "access_token" in response.json()