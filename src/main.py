from ingestion_manager import process_file
from preprocessing_engine import preprocess
from transformation_engine import transform
from retention_manager import archive_files


def main():

    files = [
        ("customers_20260713.json", "customers.parquet"),
        ("claims_20260713.json", "claims.parquet"),
        ("policies_20260713.json", "policies.parquet"),
        ("payments_20260713.json", "payments.parquet"),
        ("agents_20260713.json", "agents.parquet")
    ]

    print("========== INGESTION + PREPROCESSING ==========")

    for json_file, parquet_file in files:

        df = process_file(json_file)

        preprocess(df, parquet_file)

    print("\n========== TRANSFORMATION ==========")

    transform()

    print("\n========== RETENTION ==========")

    archive_files()

    print("\nPipeline Executed Successfully")


if __name__ == "__main__":

    main()