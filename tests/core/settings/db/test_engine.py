"""mythings.core.settings.db.engine.py tests."""

from __future__ import annotations
from pytest_check import check
from mythings.core.settings.db import engine
from mythings.core.settings.db.server import ServerDBSettings
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


def test_create_engine_returns_AsyncEngine() -> None:
    assert isinstance(engine.create_engine(), engine.AsyncEngine)


def test_create_engine_default_is_sqlite(mocker: MockerFixture) -> None:
    mock_engine = mocker.patch(
        "mythings.core.settings.db.engine.create_async_engine",
        return_value="default_engine"
    )

    result = engine.create_engine()
    assert result == mock_engine.return_value
    mock_engine.assert_called_once()

    # Tuple represents positional args, `_` are kwargs
    (url_passed,), _ = mock_engine.call_args
    with check:
        assert url_passed.drivername == "sqlite+aiosqlite"
        assert url_passed.database.endswith("mythings.db")


def test_create_engine_builds_engine(mocker: MockerFixture) -> None:
    mock_engine = mocker.patch(
        "mythings.core.settings.db.engine.create_async_engine",
        return_value="custom_engine"
    )
    test_settings = ServerDBSettings()

    result = engine.create_engine(test_settings)
    assert result == mock_engine.return_value
    mock_engine.assert_called_once()

    # Tuple represents positional args, `_` are kwargs
    (url_passed, ), _ = mock_engine.call_args
    with check:
        assert url_passed.drivername == "postgresql+asyncpg"
        assert url_passed.username == test_settings.user
        assert url_passed.password == test_settings.password.get_secret_value()
        assert url_passed.host == test_settings.host
        assert url_passed.port == test_settings.port
        assert url_passed.database == test_settings.name
