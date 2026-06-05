"""ABC for DB."""

from __future__ import annotations
from abc import ABC, abstractmethod
from pydantic import BaseModel
from .backends import DBBackend
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .url_params import SqlAlchemyUrlParams


class CoreDBSettings(BaseModel, ABC):
    """ABC for RDBMS settings."""

    backend: DBBackend

    @property
    @abstractmethod
    def url_params(self) -> SqlAlchemyUrlParams:
        """Contract of returning url_params for use in sqlalchemy.URL.create."""
