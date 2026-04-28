from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

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
    db: Session = Depends(get_db),
    claims: dict[str, Any] = Depends(get_current_user_claims),
):
    session = SkillSession(**payload.model_dump())
    db.add(session)
    db.commit()
    db.refresh(session)
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
    db: Session = Depends(get_db),
    claims: dict[str, Any] = Depends(get_current_user_claims),
):
    session = db.get(SkillSession, session_id)

    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    session.status = payload.status
    db.commit()
    db.refresh(session)
    return session