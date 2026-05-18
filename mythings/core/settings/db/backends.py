"""DB Backend-related details."""

from enum import StrEnum


class DBBackend(StrEnum):
    """StrEnum of supported DB backends."""

    POSTGRESQL = "postgresql"
    MYSQL = "mysql"
    SQLITE = "sqlite"


DIALECT_MAP: dict[DBBackend, str] = {
    DBBackend.POSTGRESQL: "postgresql+asyncpg",
    DBBackend.MYSQL: "mysql+aiomysql",
    DBBackend.SQLITE: "sqlite+aiosqlite"
}


DEFAULT_PORTS: dict[DBBackend, int] = {
    DBBackend.POSTGRESQL: 5432,
    DBBackend.MYSQL: 3306
}
