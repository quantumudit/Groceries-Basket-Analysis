import pytest

from src.exception import CustomException


def test_custom_exception_str():
    try:
        raise CustomException("Test error")
    except CustomException as e:
        assert "Test error" in str(e)
