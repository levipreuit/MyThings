"""SqlAlchemy url params to pass."""

from dataclasses import dataclass
from typing import TypedDict


class SqlAlchemyUrlKwargs(TypedDict, total=False):
    """Strongly typed structure for SqlAlchemy.

    Attributes:
        drivername (str): `SqlAlchemyUrlParams.drivername`
        database (str): `SqlAlchemyUrlParams.database`
        username (str | None): `SqlAlchemyUrlParams.username`
        password (str | None): `SqlAlchemyUrlParams.password`
        host (str | None): `SqlAlchemyUrlParams.host`
        port (int | None): `SqlAlchemyUrlParams.port`
    """
    drivername: str
    database: str
    username: str | None
    password: str | None
    host: str | None
    port: int | None


@dataclass(frozen=True)
class SqlAlchemyUrlParams:
    """Defines the url_params we pass to sqlalchemy.URL.create.

    Args:
        drivername (str): Backend dialect to use
        database (str): Name (or path, if sqlite) of database
        username (str | None): Username if connecting to a db
        password (str | None): Password if connecting to a db
        host (str | None): Host if connecting to a db
        port (str | None): Port if connecting to a db
    """
    drivername: str
    database: str

    username: str | None = None
    password: str | None = None
    host: str | None = None
    port: int | None = None

    def as_dict(self) -> SqlAlchemyUrlKwargs:
        """Converts to kwargs compatible with sqlalchemy.URL.create.

        Returns:
            dict of populated keys
        """
        kwargs: SqlAlchemyUrlKwargs = {
            "drivername": self.drivername,
            "database": self.database,
        }
        if self.username is not None:
            kwargs["username"] = self.username
        if self.password is not None:
            kwargs["password"] = self.password
        if self.host is not None:
            kwargs["host"] = self.host
        if self.port is not None:
            kwargs["port"] = self.port

        return kwargs
