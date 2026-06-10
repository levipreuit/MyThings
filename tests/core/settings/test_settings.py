"""mythings.core.settings.settings.py tests."""

from __future__ import annotations
from typing import TYPE_CHECKING
from mythings.core.settings import settings

if TYPE_CHECKING:
    from _pytest.monkeypatch import MonkeyPatch


def test_settings_loads_defaults() -> None:
    core_settings = settings.Settings()
    expected_db = settings.SqliteSettings()

    assert core_settings.db == expected_db


def test_settings_discriminates_to_non_sqlite(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("MYTHINGS_DB_BACKEND", "postgresql")
    core_settings = settings.Settings()
    expected_db = settings.ServerDBSettings()

    assert type(core_settings.db) is type(expected_db)
