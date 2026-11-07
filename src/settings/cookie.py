from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict

from settings.paths import ROOT_DIR
from app.my_project.backend.application.api.cookies import Status_Somesite


class CookieSettings(BaseSettings):
    HTTPONLY: bool = True
    SAMESITE: Status_Somesite = "lax"
    SECURE: bool = True

    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        extra="ignore",
    )


cookie_settings = CookieSettings()
