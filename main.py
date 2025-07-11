"""
main.py

Entry point for executing the data processing stage of the groceries basket analysis pipeline.

This script imports and runs the DataProcessingPipeline from the src.pipelines package.
Each stage is wrapped in a try-except block to handle and log any exceptions that may occur
during execution. The logger from src.logger is used for logging the start, completion, and
any errors for each stage.

Typical usage:
    python main.py
"""

from src.exception import CustomException
from src.logger import logger
from src.pipelines.stage_01_data_processing import DataProcessingPipeline


def run_stage(stage_name: str, pipeline_cls: type) -> None:
    """
    Runs a pipeline stage with logging and exception handling.

    Args:
        stage_name (str): Name of the pipeline stage.
        pipeline_cls (type): The pipeline class to instantiate and run.

    Raises:
        CustomException: If any error occurs during the stage execution.
    """
    try:
        logger.info(">>>>>> %s started <<<<<<", stage_name)
        obj = pipeline_cls()
        obj.main()
        logger.info(">>>>>> %s completed <<<<<<\n\nx==========x", stage_name)
    except Exception as e:
        logger.error(CustomException(e))
        raise CustomException(e) from e


if __name__ == "__main__":
    run_stage("Data Processing Stage", DataProcessingPipeline)
