from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SessionCreate(BaseModel):
    requester_profile_id: int
    mentor_profile_id: int
    requested_skill: str
    message: str | None = None
    scheduled_date: datetime | None = None


class SessionStatusUpdate(BaseModel):
    status: str


class SessionOut(BaseModel):
    id: int
    requester_profile_id: int
    mentor_profile_id: int
    requested_skill: str
    message: str | None
    scheduled_date: datetime | None
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)