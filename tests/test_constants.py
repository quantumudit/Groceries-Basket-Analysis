import os

from src.constants import CONFIGS


def test_configs_path():
    assert isinstance(CONFIGS, str)
    assert os.path.exists(CONFIGS) or CONFIGS.endswith("configs.yaml")
