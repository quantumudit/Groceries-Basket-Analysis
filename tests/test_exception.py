from src.exception import CustomException


def test_custom_exception_str():
    """Test that CustomException string representation includes the original error message."""
    try:
        raise CustomException("Test error")
    except CustomException as e:
        assert "Test error" in str(e)
