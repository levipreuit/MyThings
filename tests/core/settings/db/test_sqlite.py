"""mythings.core.settings.db.sqlite tests."""

import logging
import pytest
from pytest_check import check
from mythings.core.settings.db import sqlite
from dataclasses import asdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def test_url_params_only_have_values_for_drivername_and_database() -> None:
    expected_params = ["drivername", "database"]
    sqlite_settings = sqlite.SqliteSettings()

    url_params_dict = asdict(sqlite_settings.url_params)
    populated_params = [k for k, v in url_params_dict.items() if v]

    with check:
        assert populated_params == expected_params
        assert set(populated_params) == set(expected_params)


def test_validate_db_path_returns_resolved_path(tmp_path: "Path") -> None:
    db_path = tmp_path / "MyThings.db"
    db_path.touch()

    sqlite_settings = sqlite.SqliteSettings(path=db_path)
    assert sqlite_settings.path == db_path.resolve()


def test_validate_db_path_raises_ValueError_for_bad_path(tmp_path: "Path") -> None:
    bad_path = tmp_path / "missing" / "MyThings.db"

    with pytest.raises(ValueError, match=r"Parent directory does not exist"):
        _ = sqlite.SqliteSettings(path=bad_path).path
