from datetime import datetime

from sqlalchemy import DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class SkillSession(Base):
    __tablename__ = "sessions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    requester_profile_id: Mapped[int] = mapped_column(index=True, nullable=False)
    mentor_profile_id: Mapped[int] = mapped_column(index=True, nullable=False)
    requested_skill: Mapped[str] = mapped_column(String(150), nullable=False)
    message: Mapped[str | None] = mapped_column(Text, nullable=True)
    scheduled_date: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    status: Mapped[str] = mapped_column(String(50), default="requested", nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)