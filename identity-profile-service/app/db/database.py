from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


from app.core.config import get_settings

settings = get_settings()


class Base(DeclarativeBase):
    pass


engine = create_engine(settings.database_url, echo=False)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
