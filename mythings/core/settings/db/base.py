"""ABC for DB."""

from __future__ import annotations
from abc import ABC, abstractmethod
from pydantic_settings import BaseSettings, SettingsConfigDict
from .backends import DBBackend
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .url_params import SqlAlchemyUrlParams


_RdbmsSettingsConfigDict: SettingsConfigDict = SettingsConfigDict(
    case_sensitive=False,
    env_prefix="db_",
)


class CoreDBSettings(BaseSettings, ABC):
    """ABC for RDBMS settings."""

    model_config = _RdbmsSettingsConfigDict
    backend: DBBackend

    @property
    @abstractmethod
    def url_params(self) -> SqlAlchemyUrlParams:
        """Contract of returning url_params for use in sqlalchemy.URL.create."""
