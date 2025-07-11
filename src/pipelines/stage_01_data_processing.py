"""
stage_01_data_processing.py

This module defines the data processing pipeline for the groceries basket analysis project.
It orchestrates the transformation of raw grocery transaction data into structured formats
suitable for downstream analytics and modeling. The pipeline leverages the DataProcessor class
to perform all data transformation steps, including transaction normalization and basket generation.

Typical usage:
    Run this module as a script to execute the data processing stage as part of the ETL workflow.

Dependencies:
    - src.components.data_processor.DataProcessor
    - src.logger.logger
    - src.exception.CustomException
"""

from src.components.data_processor import DataProcessor
from src.exception import CustomException
from src.logger import logger


class DataProcessingPipeline:
    """
    Orchestrates the data processing stage of the groceries basket analysis pipeline.

    This class manages the execution of data transformation tasks, including normalization
    of transaction data and generation of product basket combinations, by utilizing the
    DataProcessor class.
    """

    def __init__(self) -> None:
        """
        Initializes the DataProcessingPipeline.
        """
        # No initialization required for now; placeholder for future extensions.

    def main(self) -> None:
        """
        Executes the data processing pipeline.

        This method instantiates the DataProcessor and runs the data transformation process.
        Logs the start and completion of the process, and handles any exceptions that occur.

        Raises:
            CustomException: If any error occurs during the data processing stage.
        """
        try:
            logger.info("Data transformation started")
            data_processor = DataProcessor()
            data_processor.data_transformation()
            logger.info("Data transformation completed successfully")
        except Exception as excp:
            logger.error(CustomException(excp))
            raise CustomException(excp) from excp


if __name__ == "__main__":
    STAGE_NAME = "Data Processing Stage"

    try:
        logger.info(">>>>>> %s started <<<<<<", STAGE_NAME)
        obj = DataProcessingPipeline()
        obj.main()
        logger.info(">>>>>> %s completed <<<<<<\n\nx==========x", STAGE_NAME)
    except Exception as e:
        logger.error(CustomException(e))
        raise CustomException(e) from e
