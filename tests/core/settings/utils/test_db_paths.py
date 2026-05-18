"""mythings.core.settings.utils.db_paths tests."""

from __future__ import annotations
from typing import TYPE_CHECKING
import pytest
from mythings.core.settings.utils import db_paths

if TYPE_CHECKING:
    from pathlib import Path


def test_resolve_db_path_rejects_broken_symlink(tmp_path: Path) -> None:
    target_loc = tmp_path / "missing.db"
    symlink_loc: Path = tmp_path / "broken.db"
    symlink_loc.symlink_to(target_loc)

    # If any of these assertions fail, test is no good
    assert symlink_loc.is_symlink()
    assert not symlink_loc.exists()

    with pytest.raises(ValueError, match=r"Path is a broken symlink"):
        _ = db_paths.resolve_db_path(symlink_loc)


def test_resolve_db_path_rejects_missing_dir(tmp_path: Path) -> None:
    parent_dir: Path = tmp_path / "missing"
    db_path: Path = parent_dir / "MyThings.db"

    # If any of these assertions fail, test is no good
    assert not parent_dir.exists()

    with pytest.raises(ValueError, match=r"Parent directory does not exist"):
        _ = db_paths.resolve_db_path(db_path)


def test_resolve_db_path_rejects_nonregular_file(tmp_path: Path) -> None:
    db_path: Path = tmp_path / "nonregular_file"
    db_path.mkdir()

    # If any of these assertions fail, test is no good
    assert db_path.exists()
    assert db_path.is_dir()

    with pytest.raises(ValueError, match=r"Path exists but is not a regular file"):
        _ = db_paths.resolve_db_path(db_path)


def test_resolve_db_path_accepts_regular_file(tmp_path: Path) -> None:
    db_path: Path = tmp_path / "MyThings.db"
    db_path.touch()

    # If any of these assertions fail, test is no good
    assert db_path.exists()

    expected_resolve = db_path.resolve()
    assert db_paths.resolve_db_path(db_path) == expected_resolve
