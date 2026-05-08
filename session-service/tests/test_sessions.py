from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_sessions_require_auth():
    response = client.get("/api/v1/sessions")
    
    assert response.status_code == 401