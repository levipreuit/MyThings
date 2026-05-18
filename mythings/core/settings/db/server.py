"""DB Server implementation of `CoreDBSettings`."""

import secrets
from pydantic import SecretStr, Field
from .base import CoreDBSettings
from .backends import (
    DBBackend,
    DIALECT_MAP,
    DEFAULT_PORTS,
)
from .url_params import SqlAlchemyUrlParams


class ServerDBSettings(CoreDBSettings):
    """Database settings for non-sqlite databases.

    Args:
        user (str): reads from DB_USER
        password (SecretStr): reads from DB_PASSWORD
        host (str): reads from DB_HOST
        port (int): reads from DB_PORT
        name (str): reads from DB_NAME
    """
    backend: DBBackend = Field(
        default=DBBackend.POSTGRESQL
    )
    user: str = "MyThings"
    password: SecretStr = Field(
        default_factory=lambda: SecretStr(secrets.token_urlsafe(64)))
    host: str = "MyThingsDb"
    port: int = Field(default_factory=lambda data: DEFAULT_PORTS[data['backend']])
    name: str = "MyThings"

    @property
    def url_params(self) -> SqlAlchemyUrlParams:
        """Provides `dict` of kwargs to be used in URL.create.

        Returns:
            Basic keyword arguments used by SQLAlchemy
        """
        return SqlAlchemyUrlParams(
            drivername=DIALECT_MAP[self.backend],
            username=self.user,
            password=self.password.get_secret_value(),
            host=self.host,
            port=self.port or DEFAULT_PORTS[self.backend],
            database=self.name,
        )
