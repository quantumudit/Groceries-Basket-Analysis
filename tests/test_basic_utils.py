import os

import pytest
from box import Box

from src.utils import basic_utils


def test_read_yaml(tmp_path):
    yaml_content = "key: value"
    yaml_file = tmp_path / "test.yaml"
    yaml_file.write_text(yaml_content)
    result = basic_utils.read_yaml(str(yaml_file))
    assert isinstance(result, Box)
    assert result.key == "value"


def test_create_directories(tmp_path):
    dir1 = tmp_path / "dir1"
    dir2 = tmp_path / "dir2"
    basic_utils.create_directories([str(dir1), str(dir2)], verbose=False)
    assert dir1.exists() and dir2.exists()


def test_dict_to_table():
    data = {"a": 1, "b": 2}
    table = basic_utils.dict_to_table(data, "Test Table")
    assert hasattr(table, "add_row")
