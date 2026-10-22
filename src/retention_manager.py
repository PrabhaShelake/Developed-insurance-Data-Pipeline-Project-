import os
import shutil

from audit_logger import log_retention

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INGESTION_FOLDER = os.path.join(BASE_DIR, "data", "ingestion")
ARCHIVE_FOLDER = os.path.join(BASE_DIR, "data", "retention", "archive")

os.makedirs(ARCHIVE_FOLDER, exist_ok=True)


def archive_files():

    files = os.listdir(INGESTION_FOLDER)

    for file in files:

        source = os.path.join(INGESTION_FOLDER, file)

        destination = os.path.join(ARCHIVE_FOLDER, file)

        shutil.move(source, destination)

        log_retention(
            file,
            "SUCCESS",
            1,
            "File Archived Successfully"
        )

    print("All files archived successfully.")


if __name__ == "__main__":

    archive_files()