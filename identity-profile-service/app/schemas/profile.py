from pydantic import BaseModel, ConfigDict


class ProfileCreate(BaseModel):
    user_id: int
    full_name: str
    bio: str | None = None
    city: str | None = None
    can_teach: str | None = None
    wants_to_learn: str | None = None


class ProfileUpdate(BaseModel):
    full_name: str | None = None
    bio: str | None = None
    city: str | None = None
    can_teach: str | None = None
    wants_to_learn: str | None = None
    is_active: bool | None = None


class ProfileOut(BaseModel):
    id: int
    user_id: int
    full_name: str
    bio: str | None
    city: str | None
    can_teach: str | None
    wants_to_learn: str | None
    is_active: bool

    model_config = ConfigDict(from_attributes=True)