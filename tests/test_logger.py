from src.logger import logger


def test_logger_info(caplog):
    """Test that logger.info outputs the expected log message at INFO level."""
    with caplog.at_level("INFO"):
        logger.info("Test log message")
    assert any(
        "Test log message" in message for message in caplog.text.splitlines()
    )
