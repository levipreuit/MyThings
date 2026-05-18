"""mythings.core.settings.db.url_params tests."""

from __future__ import annotations
from mythings.core.settings.db import url_params
from pytest_check import check
from polyfactory.factories import DataclassFactory
from dataclasses import asdict


def test_as_dict_returns_SqlAlchemyUrlKwargs() -> None:
    test_params = url_params.SqlAlchemyUrlParams(
        drivername="postgresql",
        database="MyThings")

    returned_kwargs = test_params.as_dict()

    _ = check.is_instance(returned_kwargs, dict)


def test_as_dict_returns_only_populated_SqlAlchemyUrlKwargs() -> None:
    class SqlAlchemyUrlParamsFactory(DataclassFactory[url_params.SqlAlchemyUrlParams]):
        __model__ = url_params.SqlAlchemyUrlParams
        __allow_none_optionals__ = True

    mock_url_params_coverage = SqlAlchemyUrlParamsFactory.coverage()
    for mock_url_params in mock_url_params_coverage:
        populated_params = {
            k: v for k, v in asdict(mock_url_params).items() if v}.keys()

        returned_kwargs: url_params.SqlAlchemyUrlKwargs = mock_url_params.as_dict()
        with check:
            # Make sure we didn't get a duplicated key somehow
            assert len(set(returned_kwargs.keys())) == len(returned_kwargs.keys())
            assert set(returned_kwargs.keys()) == set(populated_params)
