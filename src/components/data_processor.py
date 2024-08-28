"""
summary
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
    summary
    """

    def __init__(self):
        # Read the configuration files
        self.configs = read_yaml(CONFIGS).data_processor

        # Inputs
        self.external_data_path = normpath(self.configs.external_data_path)

        # Output file paths
        self.transactions_data_path = normpath(self.configs.transactions_data_path)
        self.basket_data_path = normpath(self.configs.basket_data_path)

    def data_transformation(self):
        """_summary_

        Raises:
            CustomException: _description_

        Returns:
            _type_: _description_
        """
        try:
            # create save directory if not exists
            create_directories(
                [dirname(self.transactions_data_path), dirname(self.basket_data_path)]
            )

            # import the dataset
            df = pd.read_csv(self.external_data_path)
            logger.info("Dataset imported")

            # Add an index column
            custom_index_col = pd.RangeIndex(
                start=10000, stop=10000 + len(df), step=1, name="id"
            )
            df.index = custom_index_col
            df.index = "TRAN" + df.index.astype("string")
            df = df.reset_index()
            logger.info("Added a unique row ID for each distinct row")

            # Unpivot the data
            df_unpivot = (
                pd.melt(df, id_vars=["id"], value_name="Products")
                .drop(columns="variable")
                .dropna()
                .sort_values(by="id")
                .rename(columns={"id": "TransactionID"})
                .reset_index(drop=True)
            )
            logger.info("Unpivoted the products")

            # Title case the product names
            df_unpivot["Products"] = df_unpivot["Products"].str.title()
            logger.info("Product names are changed from lower case to title case")

            # Export the transactions data
            df_unpivot.to_csv(self.transactions_data_path, index=False)
            logger.info("Transactions data saved at: %s", self.transactions_data_path)

            # Generate all 2-combination pairs for the available products
            combinations_list = list(
                combinations(df_unpivot["Products"].unique().tolist(), 2)
            )
            logger.info("Generated all combination pairs of available products")

            # Create a new DataFrame with the combinations
            df_basket = pd.DataFrame(
                combinations_list, columns=["Product-1", "Product-2"]
            )
            logger.info("Created the basket dataframe")

            # Create a basket column
            df_basket["Basket"] = (
                df_basket["Product-1"] + " + " + df_basket["Product-2"]
            )
            logger.info("Created a basket column")

            # Export the Baskets data
            df_basket.to_csv(self.basket_data_path, index=False)
            logger.info("Basket data saved at: %s", self.basket_data_path)

            return None
        except Exception as e:
            logger.error(CustomException(e))
            raise CustomException(e) from e
