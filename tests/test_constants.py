import os

from src.constants import CONFIGS


def test_configs_path():
    """Test that CONFIGS is a string and points to a valid or expected config file path."""
    assert isinstance(CONFIGS, str)
    assert os.path.exists(CONFIGS) or CONFIGS.endswith("configs.yaml")
