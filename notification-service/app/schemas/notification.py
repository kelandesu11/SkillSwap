from datetime import datetime

from pydantic import BaseModel, ConfigDict


class NotificationCreate(BaseModel):
    profile_id: int
    message: str
    type: str
    status: str = "pending"


class NotificationOut(BaseModel):
    id: int
    profile_id: int
    message: str
    type: str
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)