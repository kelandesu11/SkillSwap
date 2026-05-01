from typing import Any

from fastapi import APIRouter, Depends, Header, HTTPException, Query, Request
from sqlalchemy.orm import Session

from app.clients.identity_client import validate_profile_exists
from app.clients.notification_client import create_notification
from app.core.auth import get_current_user_claims
from app.db.database import SessionLocal
from app.models.session import SkillSession
from app.schemas.session import SessionCreate, SessionOut, SessionStatusUpdate

router = APIRouter(prefix="/api/v1/sessions", tags=["sessions"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", response_model=SessionOut)
def create_session(
    payload: SessionCreate,
    request: Request,
    authorization: str = Header(...),
    db: Session = Depends(get_db),
    claims: dict[str, Any] = Depends(get_current_user_claims),
):
    request_id = request.state.request_id
    
    validate_profile_exists(payload.requester_profile_id, authorization)
    validate_profile_exists(payload.mentor_profile_id, authorization)

    session = SkillSession(**payload.model_dump())
    db.add(session)
    db.commit()
    db.refresh(session)

    create_notification(
        profile_id=payload.mentor_profile_id,
        message=f"New session request for {payload.requested_skill}",
        request_id=request_id,
        notification_type="session_requested",
        authorization=authorization,
    )

    return session


@router.get("", response_model=list[SessionOut])
def list_sessions(
    status: str | None = Query(default=None),
    db: Session = Depends(get_db),
    claims: dict[str, Any] = Depends(get_current_user_claims),
):
    query = db.query(SkillSession)

    if status:
        query = query.filter(SkillSession.status == status)

    return query.all()


@router.get("/{session_id}", response_model=SessionOut)
def get_session(
    session_id: int,
    db: Session = Depends(get_db),
    claims: dict[str, Any] = Depends(get_current_user_claims),
):
    session = db.get(SkillSession, session_id)

    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    return session


@router.patch("/{session_id}/status", response_model=SessionOut)
def update_session_status(
    session_id: int,
    payload: SessionStatusUpdate,
    request: Request,
    authorization: str = Header(...),
    db: Session = Depends(get_db),
    claims: dict[str, Any] = Depends(get_current_user_claims),
):
    request_id = request.state.request_id

    session = db.get(SkillSession, session_id)

    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    session.status = payload.status
    db.commit()
    db.refresh(session)

    if payload.status in {"approved", "rejected", "cancelled"}:
        create_notification(
            profile_id=session.requester_profile_id,
            message=f"Your session request for {session.requested_skill} was {payload.status}",
            notification_type=f"session_{payload.status}",
            authorization=authorization,
            request_id=request_id,
        )

    return session