"""Utilities relating to paths."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Generator


def describe_path_type(p: Path) -> str:
    """Provides short description of the type of path passed.

    Args:
        p (Path): Path to describe

    Returns:
        Short description (os-oriented)
    """
    type_map: dict[str, bool] = {
        "file": p.is_file(),
        "directory": p.is_dir(),
        "mount point": p.is_mount(),
        "block device": p.is_block_device(),
        "character device": p.is_char_device(),
        "named pipe": p.is_fifo(),
        "socket": p.is_socket()
    }
    matched: Generator[str] = (
        pth_type for pth_type, is_type in type_map.items() if is_type)
    path_type_known: str | None = next(matched, None)
    return path_type_known or "unknown non-regular file"
