"""Top-level settings module."""

from __future__ import annotations
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from mythings.core.settings.db import SqliteSettings, ServerDBSettings


class Settings(BaseSettings):
    """Top-level settings."""

    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_prefix="MYTHINGS_",
        env_nested_delimiter="_",
        env_nested_max_split=1,
    )

    db: SqliteSettings | ServerDBSettings = Field(
        default_factory=SqliteSettings, discriminator="backend"
    )

    currency: str = Field(default="USD")
