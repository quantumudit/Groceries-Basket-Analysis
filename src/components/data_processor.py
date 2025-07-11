"""
data_processor.py

This module provides the DataProcessor class for handling the transformation of raw grocery transaction data
into structured formats suitable for basket analysis and further data mining tasks.

Key functionalities:
- Reads configuration settings for input and output file paths.
- Loads raw transaction data from a CSV file.
- Assigns unique transaction IDs to each row.
- Unpivots the data to create a normalized transactions table.
- Standardizes product names to title case for consistency.
- Saves the processed transactions data to a specified output location.
- Generates all possible 2-item product combinations (baskets) for market basket analysis.
- Saves the generated basket data to a specified output location.
- Handles errors gracefully and logs key processing steps for traceability.

Intended for use in grocery basket analysis projects where preprocessing and transformation of transaction data
is required prior to association rule mining or visualization.
"""

from itertools import combinations
from os.path import dirname, normpath

import pandas as pd

from src.constants import CONFIGS
from src.exception import CustomException
from src.logger import logger
from src.utils.basic_utils import create_directories, read_yaml


class DataProcessor:
    """
    Handles the transformation of raw grocery transaction data into structured formats
    for transaction and basket analysis, based on project configurations.
    """

    def __init__(self) -> None:
        # Read the configuration files
        self.configs = read_yaml(CONFIGS).data_processor

        # Inputs
        self.external_data_path = normpath(self.configs.external_data_path)

        # Output file paths
        self.transactions_data_path = normpath(
            self.configs.transactions_data_path
        )
        self.basket_data_path = normpath(self.configs.basket_data_path)

    def data_transformation(self) -> None:
        """
        Transforms raw grocery transaction data from a CSV file into structured formats
        for transaction and basket analysis.

        Reads the input CSV file (self.external_data_path), assigns unique transaction IDs, unpivots the data,
        standardizes product names, and saves the processed transactions to self.transactions_data_path (CSV).
        Generates all possible 2-item product combinations and saves the basket data to self.basket_data_path (CSV).

        Input:
            - Raw transaction data CSV file (no header, products per row)
        Output:
            - Transactions CSV file (TransactionID, Products)
            - Basket CSV file (Product-1, Product-2, Basket)

        Raises:
            CustomException: If any error occurs during processing.
        """
        try:
            self._create_output_directories()
            df = self._import_dataset()
            df = self._add_unique_row_id(df)
            df_unpivot = self._unpivot_data(df)
            df_unpivot = self._standardize_product_names(df_unpivot)
            self._export_transactions(df_unpivot)
            df_basket = self._generate_basket_combinations(df_unpivot)
            self._export_baskets(df_basket)
        except Exception as e:
            logger.error(CustomException(e))
            raise CustomException(e) from e

    def _create_output_directories(self) -> None:
        create_directories(
            [
                dirname(self.transactions_data_path),
                dirname(self.basket_data_path),
            ]
        )
        logger.info("Output directories ensured.")

    def _import_dataset(self) -> pd.DataFrame:
        df = pd.read_csv(self.external_data_path, header=None)
        logger.info("Dataset imported from %s", self.external_data_path)
        return df

    def _add_unique_row_id(self, df: pd.DataFrame) -> pd.DataFrame:
        custom_index_col = pd.RangeIndex(
            start=10000, stop=10000 + len(df), step=1, name="id"
        )
        df.index = custom_index_col
        df.index = "TRAN" + df.index.astype("string")
        df = df.reset_index()
        logger.info("Added a unique row ID for each distinct row")
        return df

    def _unpivot_data(self, df: pd.DataFrame) -> pd.DataFrame:
        df_unpivot = (
            pd.melt(df, id_vars=["id"], value_name="Products")
            .drop(columns="variable")
            .dropna()
            .sort_values(by="id")
            .rename(columns={"id": "TransactionID"})
            .reset_index(drop=True)
        )
        logger.info("Unpivoted the products")
        return df_unpivot

    def _standardize_product_names(
        self, df_unpivot: pd.DataFrame
    ) -> pd.DataFrame:
        df_unpivot["Products"] = df_unpivot["Products"].str.title()
        logger.info("Product names standardized to title case")
        return df_unpivot

    def _export_transactions(self, df_unpivot: pd.DataFrame) -> None:
        df_unpivot.to_csv(self.transactions_data_path, index=False)
        logger.info(
            "Transactions data saved at: %s", self.transactions_data_path
        )

    def _generate_basket_combinations(
        self, df_unpivot: pd.DataFrame
    ) -> pd.DataFrame:
        combinations_list = list(
            combinations(df_unpivot["Products"].unique().tolist(), 2)
        )
        logger.info("Generated all combination pairs of available products")
        df_basket = pd.DataFrame(
            combinations_list, columns=["Product-1", "Product-2"]
        )
        df_basket["Basket"] = (
            df_basket["Product-1"] + " + " + df_basket["Product-2"]
        )
        logger.info("Created the basket dataframe and basket column")
        return df_basket

    def _export_baskets(self, df_basket: pd.DataFrame) -> None:
        df_basket.to_csv(self.basket_data_path, index=False)
        logger.info("Basket data saved at: %s", self.basket_data_path)
