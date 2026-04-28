from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.auth import get_current_user_claims
from app.db.database import SessionLocal
from app.models.notification import Notification
from app.schemas.notification import NotificationCreate, NotificationOut

router = APIRouter(prefix="/api/v1/notifications", tags=["notifications"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", response_model=NotificationOut)
def create_notification(
    payload: NotificationCreate,
    db: Session = Depends(get_db),
    claims: dict[str, Any] = Depends(get_current_user_claims),
):
    notification = Notification(**payload.model_dump())
    db.add(notification)
    db.commit()
    db.refresh(notification)
    return notification


@router.get("", response_model=list[NotificationOut])
def list_notifications(
    db: Session = Depends(get_db),
    claims: dict[str, Any] = Depends(get_current_user_claims),
):
    return db.query(Notification).all()


@router.get("/profile/{profile_id}", response_model=list[NotificationOut])
def get_notifications_by_profile(
    profile_id: int,
    db: Session = Depends(get_db),
    claims: dict[str, Any] = Depends(get_current_user_claims),
):
    return db.query(Notification).filter(Notification.profile_id == profile_id).all()


@router.get("/{notification_id}", response_model=NotificationOut)
def get_notification(
    notification_id: int,
    db: Session = Depends(get_db),
    claims: dict[str, Any] = Depends(get_current_user_claims),
):
    notification = db.get(Notification, notification_id)

    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")

    return notification