"""mythings.core.utils.db_paths tests."""

from __future__ import annotations
from typing import TYPE_CHECKING
from mythings.core.utils import paths

if TYPE_CHECKING:
    from pathlib import Path


def test_paths_describes_dir(tmp_path: Path) -> None:
    dir_path: Path = tmp_path / "directory"
    dir_path.mkdir()

    expected_path_type = "directory"

    assert paths.describe_path_type(dir_path) == expected_path_type


def test_paths_describes_reg_file(tmp_path: Path) -> None:
    file_path: Path = tmp_path / "file.txt"
    file_path.touch()

    expected_path_type = "file"

    assert paths.describe_path_type(file_path) == expected_path_type
