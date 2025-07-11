"""
exception.py

This module provides custom error handling utilities for the project.
It includes a function for extracting detailed error information and a custom exception class
that enhances error messages with file and line number context.

Key functionalities:
    - error_details: Retrieves the file name and line number where an error occurred.
    - CustomException: Exception subclass that formats error messages with context for easier debugging.

Intended usage:
    Use CustomException throughout the project to raise and log errors with detailed context.
"""

import sys


def error_details(error: Exception) -> str:
    """
    Retrieves detailed information about an error, including the file name and line number.

    Args:
        error (Exception): The error object.

    Returns:
        str: A formatted error message with file name and line number.
    """
    _, _, exc_tb = sys.exc_info()
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "<unknown>"
        line_number = -1
    error_message = f"Error occurred in Python script [{file_name}] at line [{line_number}]: [{str(error)}]"
    return error_message


class CustomException(Exception):
    """
    Custom exception class that provides detailed error messages including file name and line number.

    Args:
        error_message (Exception): The original exception or error message.

    Attributes:
        error_message (str): The formatted error message with context.
    """

    def __init__(self, error_message: Exception) -> None:
        super().__init__(error_message)
        self.error_message = error_details(error_message)

    def __str__(self) -> str:
        return self.error_message
