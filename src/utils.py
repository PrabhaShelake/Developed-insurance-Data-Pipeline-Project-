import os
import json
from datetime import datetime

import pandas as pd


def read_json(file_path):
    """
    Reads a JSON control file and returns its contents as a dictionary.
    """

    with open(file_path, "r") as file:
        data = json.load(file)

    return data


def read_csv(file_path):
    """
    Reads a CSV file and returns a Pandas DataFrame.
    """

    return pd.read_csv(file_path)


def write_parquet(dataframe, output_path):
    """
    Saves a DataFrame as a Parquet file.
    """

    dataframe.to_parquet(output_path, index=False)


def create_directory(directory_path):
    """
    Creates a directory if it does not already exist.
    """

    os.makedirs(directory_path, exist_ok=True)


def file_exists(file_path):
    """
    Checks whether a file exists.
    """

    return os.path.exists(file_path)


def get_current_date():
    """
    Returns today's date in YYYYMMDD format.
    """

    return datetime.now().strftime("%Y%m%d")