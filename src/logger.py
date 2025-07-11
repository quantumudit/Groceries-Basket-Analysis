"""
logger.py

This module configures and provides a logger for the project.
It creates a timestamped log file in a dedicated logs directory and sets up logging to both
file and console with a standardized format for easy debugging and traceability.

Key functionalities:
    - Ensures a 'logs' directory exists in the current working directory.
    - Generates a log file with a unique timestamp for each run.
    - Configures logging to output to both the log file and the console.
    - Provides a logger object for use throughout the project.

Typical usage:
    from src.logger import logger
    logger.info("Your log message here")
"""

import logging
import os
import sys
from datetime import datetime

# Ensure logs directory exists in the current working directory
logs_dir_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir_path, exist_ok=True)

# Generate a timestamped log file name
timestamp_fmt = datetime.now().strftime("%Y_%m_%d_%I_%M_%S_%p")
logs_filename = f"{timestamp_fmt}.log"

# Full path to the log file
LOG_FILE_PATH = os.path.join(logs_dir_path, logs_filename)

# Logging format string
LOGGING_STR = "[%(asctime)s]:%(name)s %(levelname)s:%(module)s %(lineno)d - %(message)s"

# Configure logging to file and console
logging.basicConfig(
    level=logging.INFO,
    encoding="utf-8",
    format=LOGGING_STR,
    datefmt="%Y-%m-%d %I:%M:%S %p",
    handlers=[logging.FileHandler(LOG_FILE_PATH), logging.StreamHandler(sys.stdout)],
)

# Project-wide logger object
logger = logging.getLogger("ProjectLogger")
