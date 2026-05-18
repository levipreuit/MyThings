"""Utilities for db paths."""

from __future__ import annotations
from typing import TYPE_CHECKING
from mythings.core.utils import paths

if TYPE_CHECKING:
    from pathlib import Path


def resolve_db_path(loc: Path) -> Path:
    """Function to help with resolving db path, similar to pydantic approach.

    Args:
        loc (Path): DB path being resolved

    Returns:
        Path passed in, so long as it resolved to an actual file/symlink to a file.

    Raises:
        ValueError: Pydantic-expected raises for failed validations.
    """
    msg: str
    if loc.is_symlink() and not loc.exists():
        msg = (
            "Path is a broken symlink:"
            f"{loc} -> {loc.readlink()}"
        )
        raise ValueError(msg)
    resolved = loc.resolve()
    if not resolved.parent.is_dir():
        msg = (
            "Parent directory does not exist:"
            f"{resolved.parent}"
        )
        raise ValueError(msg)
    if resolved.exists() and not resolved.is_file():
        msg = (
            "Path exists but is not a regular file:"
            f"{resolved} is a {paths.describe_path_type(resolved)}"
            )
        raise ValueError(msg)
    return resolved
