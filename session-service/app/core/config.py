from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Session Service"
    app_version: str = "0.1.0"
    database_url: str = "postgresql+psycopg://postgres:Km15578!@postgres:5432/sessions_db"

    jwt_secret_key: str = "secret-key"
    jwt_algorithm: str = "HS256"

    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore",
        )
    

@lru_cache
def get_settings() -> Settings:
    return Settings()