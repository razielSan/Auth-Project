from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

from settings.paths import ROOT_DIR


class Settings(BaseSettings):
    DATABASE_CONNECT: str

    # SQLAlchemy settings
    DB_POOL_SIZE: int = Field(default=5, ge=1)
    DB_MAX_OVERFLOW: int = Field(default=10, ge=0)
    DB_ECHO: bool

    # Redis settings
    REDIS_HOST: str
    REDIS_PORT: int

    # JWT settings
    SECRET_KEY_TOKEN: str
    SECRET_KEY_TOKEN_REFRESH: str
    ALGORITHM_TOKEN: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int

    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        extra="ignore",
    )


settings = Settings()
