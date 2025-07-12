"""
basic_utils.py

This module provides utility functions for file and directory operations, YAML handling,
and data presentation for the groceries basket analysis project.

Key functionalities:
    - Reading YAML files into Box objects for easy attribute access.
    - Creating directories with logging and error handling.
    - Converting dictionaries to rich tables for console display.

All functions are designed to handle exceptions gracefully and log relevant information
for debugging and traceability.

Dependencies:
    - box.Box
    - rich.table.Table
    - src.logger.logger
    - src.exception.CustomException
"""

from os import makedirs
from os.path import normpath

import yaml
from box import Box
from rich.table import Table

from src.exception import CustomException
from src.logger import logger


def read_yaml(yaml_path: str) -> Box:
    """
    Reads a YAML file from the provided path and returns its content as a Box object.

    Args:
        yaml_path (str): Path to the YAML file to be read.

    Returns:
        Box: Content of the YAML file, loaded into a Box object for easy access.

    Raises:
        CustomException: If there is any error while reading or parsing the file.
    """
    try:
        yaml_path = normpath(yaml_path)
        with open(yaml_path, encoding="utf-8") as yf:
            content = Box(yaml.safe_load(yf))
            logger.info("YAML file loaded successfully: %s", yaml_path)
            return content
    except Exception as e:
        logger.error(CustomException(e))
        raise CustomException(e) from e


def create_directories(dir_paths: list[str], verbose: bool = True) -> None:
    """
    Creates directories at the specified paths.

    Args:
        dir_paths (list[str]): List of directory paths to create.
        verbose (bool, optional): If True, logs a message for each directory created. Defaults to True.
    """
    for path in dir_paths:
        makedirs(normpath(path), exist_ok=True)
        if verbose:
            logger.info("Created directory at: %s", path)


def dict_to_table(data: dict, title: str) -> Table:
    """
    Converts a dictionary to a rich Table for console display.

    Args:
        data (dict): Dictionary to display.
        title (str): Title for the table.

    Returns:
        Table: A rich Table object representing the dictionary.
    """
    table = Table(title=title)
    table.add_column(
        "Dataframe Attributes", justify="left", style="bright_cyan", no_wrap=True
    )
    table.add_column("Value", justify="right", style="bright_magenta")
    for key, value in data.items():
        table.add_row(key, str(value))
    return table
