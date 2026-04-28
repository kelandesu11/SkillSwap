from pydantic import BaseModel, EmailStr


class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str = "member"


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class RefreshRequest(BaseModel):
    refresh_token: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class CurrentUserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: str
    is_active: bool