from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.health import router as health_router
from app.api.mfa import router as mfa_router
from app.api.profiles import router as profiles_router
from app.core.config import get_settings
from app.core.middleware import RequestLoggingMiddleware
from app.db.database import Base, engine
import app.models

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.add_middleware(RequestLoggingMiddleware)

Base.metadata.create_all(bind=engine)

app.include_router(health_router)
app.include_router(auth_router)
app.include_router(profiles_router)
app.include_router(mfa_router)