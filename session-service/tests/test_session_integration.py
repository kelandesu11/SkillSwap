from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_sessions_require_auth():
    response = client.get("/api/v1/sessions")
    
    assert response.status_code == 401


def test_create_session_requires_auth():
    response = client.post(
        "/api/v1/sessions",
        json={
            "requester_profile_id": 1,
            "mentor_profile_id": 2,
            "required_skill": "Python",
            "message": "I want to learn FastAPI!",
            "scheduled_date": "2026-05-01T18:00:00",
        },
    )

    assert response.status_code == 401