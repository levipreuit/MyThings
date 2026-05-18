"""mythings.core.settings.db.server.py tests."""

from __future__ import annotations
from pytest_check import check
from mythings.core.settings.db import server


def test_url_params_returns_SqlAlchemyUrlParams() -> None:
    test_settings = server.ServerDBSettings()
    url_params = test_settings.url_params

    _ = check.is_instance(url_params, server.SqlAlchemyUrlParams)
