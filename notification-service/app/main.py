from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.notifications import router as notifications_router
from app.core.config import get_settings
from app.db.database import Base, engine
import app.models

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

Base.metadata.create_all(bind=engine)

app.include_router(health_router)
app.include_router(notifications_router)