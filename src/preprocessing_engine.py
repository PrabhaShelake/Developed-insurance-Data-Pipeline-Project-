import os
import pandas as pd

from utils import write_parquet
from audit_logger import log_preprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PREPROCESSED_FOLDER = os.path.join(BASE_DIR, "data", "preprocessed")

def remove_duplicates(df):
    """
    Removes duplicate rows from the DataFrame.
    """

    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    removed = before - after

    return df, removed



def handle_missing_values(df):
    """
    Replace missing values.
    """

    df = df.fillna("Unknown")

    return df


def trim_spaces(df):
    """
    Removes leading and trailing spaces from text columns.
    """

    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].str.strip()

    return df


from datetime import datetime


def add_audit_columns(df):
    """
    Adds audit columns.
    """

    df["Load_Date"] = datetime.now().strftime("%Y-%m-%d")

    df["Created_By"] = "ETL_Pipeline"

    return df

def save_preprocessed(df, output_file):
    """
    Saves cleaned data as Parquet.
    """

    output_path = os.path.join(
        PREPROCESSED_FOLDER,
        output_file
    )

    write_parquet(df, output_path)

def preprocess(df, output_file):
    """
    Complete preprocessing pipeline.
    """

    df, duplicates_removed = remove_duplicates(df)

    df = handle_missing_values(df)

    df = trim_spaces(df)

    df = add_audit_columns(df)

    save_preprocessed(df, output_file)

    log_preprocess(
        output_file,
        "SUCCESS",
        len(df),
        f"{duplicates_removed} duplicate rows removed"
    )

    return df


if __name__ == "__main__":

    from ingestion_manager import process_file

    files = [
        ("customers_20260713.json", "customers.parquet"),
        ("claims_20260713.json", "claims.parquet"),
        ("policies_20260713.json", "policies.parquet"),
        ("payments_20260713.json", "payments.parquet"),
        ("agents_20260713.json", "agents.parquet")
    ]

    for json_file, parquet_file in files:

        print(f"\nProcessing {json_file}...")

        df = process_file(json_file)

        preprocess(df, parquet_file)

    print("\nAll files processed successfully.")