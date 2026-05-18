"""Sqlite implementation of `CoreDBSettings`."""

from .base import CoreDBSettings
from .backends import DBBackend, DIALECT_MAP
from .url_params import SqlAlchemyUrlParams
from mythings.core.settings.utils import db_paths
from pathlib import Path
from pydantic import Field, field_validator


class SqliteSettings(CoreDBSettings):
    """Settings specific to SQLite db setup."""
    backend: DBBackend = Field(
        default=DBBackend.SQLITE,
        frozen=True,
    )
    path: Path = Field(default=Path("mythings.db"), validate_default=True)

    @field_validator("path", mode="after")
    @classmethod
    def validate_db_path(cls, loc: Path) -> Path:
        """Performs validation of the sqlite db path.

        Args:
            loc (Path): Location of the db

        Returns:
            _description_
        """
        return db_paths.resolve_db_path(loc)

    @property
    def url_params(self) -> SqlAlchemyUrlParams:
        """Provides `dict` of kwargs to be used in URL.create.

        Returns:
            Basic keyword arguments used by SQLAlchemy
        """
        return SqlAlchemyUrlParams(
            drivername=DIALECT_MAP[self.backend],
            database=str(self.path),
        )
