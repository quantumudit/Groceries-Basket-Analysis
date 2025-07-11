from src.logger import logger


def test_logger_info(caplog):
    with caplog.at_level("INFO"):
        logger.info("Test log message")
    assert any(
        "Test log message" in message for message in caplog.text.splitlines()
    )
