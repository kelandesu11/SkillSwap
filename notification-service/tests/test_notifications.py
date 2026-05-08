from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_notifications_require_auth():
    response = client.get("/api/v1/notifications")
    

    assert response.status_code == 401