import csv
import os
from datetime import datetime

# Log folder path
LOG_FOLDER = "../logs"

# Create logs folder if it doesn't exist
os.makedirs(LOG_FOLDER, exist_ok=True)


def write_log(log_file, file_name, status, records, message):
    """
    Writes a log entry into the specified CSV log file.
    """

    log_path = os.path.join(LOG_FOLDER, log_file)

    file_exists = os.path.isfile(log_path)

    with open(log_path, mode="a", newline="") as file:
        writer = csv.writer(file)

        # Write header only if the file is new
        if not file_exists:
            writer.writerow([
                "Timestamp",
                "File_Name",
                "Status",
                "Records",
                "Message"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            file_name,
            status,
            records,
            message
        ])


def log_ingestion(file_name, status, records, message):
    write_log(
        "ingestion_log.csv",
        file_name,
        status,
        records,
        message
    )


def log_preprocess(file_name, status, records, message):
    write_log(
        "preprocess_log.csv",
        file_name,
        status,
        records,
        message
    )


def log_retention(file_name, status, records, message):
    write_log(
        "retention_log.csv",
        file_name,
        status,
        records,
        message
    )


# Test the logger
if __name__ == "__main__":

    log_ingestion(
        "customers_20260713.csv",
        "SUCCESS",
        500,
        "File Loaded Successfully"
    )

    log_preprocess(
        "customers_20260713.csv",
        "SUCCESS",
        500,
        "Duplicates Removed"
    )

    log_retention(
        "customers_20260713.csv",
        "SUCCESS",
        500,
        "Archived Successfully"
    )

    print("CSV Logs Created Successfully")

