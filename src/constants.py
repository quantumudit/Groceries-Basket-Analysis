"""
constants.py

This module defines global constants for the groceries basket analysis project.
It provides normalized paths to configuration and schema files, ensuring compatibility
across different operating systems.

Constants:
    CONFIGS (str): Normalized path to the main YAML configuration file.
    # Add other constants here as needed, e.g., SCHEMA = normpath("conf/schema.yaml")

Intended usage:
    Import these constants wherever configuration or schema file paths are required.
"""

from os.path import normpath

CONFIGS = normpath("conf/configs.yaml")
