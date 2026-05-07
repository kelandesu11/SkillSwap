from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_register_login_and_me_flow():
    register_response = client.post(
        "/api/v1/auth/register",
        json={
            "username": "integrationuser",
            "email": "integration@example.com",
            "password": "password123",
        },
    )

    assert register_response.status_code in [201, 400]

    login_response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "integration@example.com",
            "password": "password123",
        },
    )

    assert login_response.status_code == 200

    token = login_response.json().get("access_token")

    me_response = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert me_response.status_code == 200
    assert me_response.json().get("email") == "integration@example.com"