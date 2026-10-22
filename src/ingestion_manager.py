import os

from utils import read_json, read_csv, file_exists
from audit_logger import log_ingestion

# Project folders
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG_FOLDER = os.path.join(BASE_DIR, "config", "control_files")
INGESTION_FOLDER = os.path.join(BASE_DIR, "data", "ingestion")

def load_control_file(json_file):
    """
    Reads the JSON control file.
    """

    json_path = os.path.join(CONFIG_FOLDER, json_file)

    return read_json(json_path)


def load_csv_file(csv_file):
    """
    Reads a CSV file from the ingestion folder.
    """

    csv_path = os.path.join(INGESTION_FOLDER, csv_file)

    if not file_exists(csv_path):

        log_ingestion(
            csv_file,
            "FAILED",
            0,
            "CSV File Not Found"
        )

        raise FileNotFoundError(f"{csv_file} not found.")

    dataframe = read_csv(csv_path)

    log_ingestion(
        csv_file,
        "SUCCESS",
        len(dataframe),
        "CSV Loaded Successfully"
    )

    return dataframe


def validate_columns(dataframe, expected_columns):
    """
    Checks whether all required columns exist.
    """

    actual_columns = dataframe.columns.tolist()

    for column in expected_columns:

        if column not in actual_columns:
            raise Exception(f"Missing Column : {column}")

    return True


def process_file(json_file):
    """
    Reads JSON configuration, loads CSV and validates columns.
    """

    config = load_control_file(json_file)

    csv_file = config["file_name"]

    dataframe = load_csv_file(csv_file)

    validate_columns(
        dataframe,
        config["expected_columns"]
    )

    return dataframe

if __name__ == "__main__":

    dataframe = process_file("customers_20260713.json")

    print(dataframe.head())