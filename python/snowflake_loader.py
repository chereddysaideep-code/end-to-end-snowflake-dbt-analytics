import os
from pathlib import Path

import pandas as pd
import snowflake.connector
from dotenv import load_dotenv


load_dotenv()

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "sample"


def get_connection():
    return snowflake.connector.connect(
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE", "ANALYTICS_DB"),
        schema=os.getenv("SNOWFLAKE_SCHEMA", "RAW"),
        role=os.getenv("SNOWFLAKE_ROLE"),
    )


def load_table(cursor, dataframe, table_name):
    columns = ", ".join(dataframe.columns)
    placeholders = ", ".join(["%s"] * len(dataframe.columns))

    insert_sql = f"""
        INSERT INTO {table_name} ({columns})
        VALUES ({placeholders})
    """

    rows = [tuple(row) for row in dataframe.itertuples(index=False, name=None)]

    cursor.executemany(insert_sql, rows)

    print(f"Loaded {len(rows)} rows into {table_name}")


def main():
    files = {
        "customers": "CUSTOMERS",
        "products": "PRODUCTS",
        "orders": "ORDERS",
        "order_items": "ORDER_ITEMS",
    }

    connection = get_connection()
    cursor = connection.cursor()

    try:
        for file_name, table_name in files.items():
            file_path = DATA_DIR / f"{file_name}.csv"

            dataframe = pd.read_csv(file_path)

            dataframe.columns = [
                column.upper()
                for column in dataframe.columns
            ]

            load_table(
                cursor,
                dataframe,
                f"ANALYTICS_DB.RAW.{table_name}",
            )

        connection.commit()
        print("Snowflake ingestion completed successfully.")

    except Exception as error:
        connection.rollback()
        print(f"Snowflake ingestion failed: {error}")
        raise

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()
