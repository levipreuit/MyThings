"""SQLAlchemy db engine module."""

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from mythings.core.settings.db import CoreDBSettings, SqliteSettings


def create_engine(settings: CoreDBSettings | None = None) -> AsyncEngine:
    """Performs the engine creation for SqlAlchemy.

    Args:
        settings (CoreDBSettings | None): Object to get the url params from

    Returns:
        Created AsyncEngine
    """
    if settings is None:
        settings = SqliteSettings()
    url = URL.create(**settings.url_params.as_dict())
    return create_async_engine(url)
