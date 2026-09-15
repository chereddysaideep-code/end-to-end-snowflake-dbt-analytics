from pathlib import Path
import pandas as pd


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "sample"


FILES = {
    "customers": "customers.csv",
    "products": "products.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
}


EXPECTED_COLUMNS = {
    "customers": {
        "customer_id",
        "customer_name",
        "country",
        "signup_date",
        "customer_segment",
    },
    "products": {
        "product_id",
        "product_name",
        "category",
        "price",
    },
    "orders": {
        "order_id",
        "customer_id",
        "order_date",
        "status",
    },
    "order_items": {
        "order_id",
        "product_id",
        "quantity",
        "unit_price",
    },
}


PRIMARY_KEYS = {
    "customers": "customer_id",
    "products": "product_id",
    "orders": "order_id",
}


# ---------------------------------------------------------
# Load data
# ---------------------------------------------------------

def load_data():
    data = {}

    for table_name, file_name in FILES.items():

        file_path = DATA_DIR / file_name

        if not file_path.exists():
            raise FileNotFoundError(
                f"Missing input file: {file_path}"
            )

        df = pd.read_csv(file_path)

        data[table_name] = df

        print(
            f"Loaded {table_name}: "
            f"{len(df):,} rows"
        )

    return data


# ---------------------------------------------------------
# Validate schema
# ---------------------------------------------------------

def validate_schema(data):

    print("\nSchema Validation")
    print("-" * 50)

    for table_name, df in data.items():

        expected = EXPECTED_COLUMNS[table_name]

        actual = set(df.columns)

        missing = expected - actual
        unexpected = actual - expected

        if missing:
            print(
                f"[FAIL] {table_name}: "
                f"Missing columns: {sorted(missing)}"
            )

        elif unexpected:
            print(
                f"[WARN] {table_name}: "
                f"Unexpected columns: {sorted(unexpected)}"
            )

        else:
            print(
                f"[PASS] {table_name}: "
                f"Schema is valid"
            )


# ---------------------------------------------------------
# Validate primary keys
# ---------------------------------------------------------

def validate_primary_keys(data):

    print("\nPrimary Key Validation")
    print("-" * 50)

    for table_name, primary_key in PRIMARY_KEYS.items():

        df = data[table_name]

        null_count = df[primary_key].isna().sum()
        duplicate_count = df[primary_key].duplicated().sum()

        if null_count == 0 and duplicate_count == 0:

            print(
                f"[PASS] {table_name}.{primary_key}: "
                f"No null or duplicate keys"
            )

        else:

            print(
                f"[FAIL] {table_name}.{primary_key}: "
                f"{null_count} nulls, "
                f"{duplicate_count} duplicates"
            )


# ---------------------------------------------------------
# Missing-value analysis
# ---------------------------------------------------------

def missing_value_analysis(data):

    print("\nMissing Value Analysis")
    print("-" * 50)

    for table_name, df in data.items():

        missing = df.isna().sum()

        missing = missing[missing > 0]

        if missing.empty:

            print(
                f"[PASS] {table_name}: "
                f"No missing values"
            )

        else:

            print(f"[WARN] {table_name}:")

            for column, count in missing.items():

                print(
                    f"    {column}: {count}"
                )


# ---------------------------------------------------------
# Business metrics
# ---------------------------------------------------------

def calculate_metrics(data):

    orders = data["orders"]
    order_items = data["order_items"]

    order_items = order_items.copy()

    order_items["line_revenue"] = (
        order_items["quantity"]
        * order_items["unit_price"]
    )

    total_revenue = order_items["line_revenue"].sum()

    completed_order_ids = set(
        orders.loc[
            orders["status"] == "Completed",
            "order_id"
        ]
    )

    completed_items = order_items[
        order_items["order_id"].isin(
            completed_order_ids
        )
    ]

    completed_revenue = (
        completed_items["line_revenue"].sum()
    )

    completed_orders = len(
        completed_order_ids
    )

    average_order_value = (
        completed_revenue / completed_orders
        if completed_orders
        else 0
    )

    print("\nBusiness Metrics")
    print("-" * 50)

    print(
        f"Total order-item revenue: "
        f"${total_revenue:,.2f}"
    )

    print(
        f"Completed orders: "
        f"{completed_orders:,}"
    )

    print(
        f"Completed-order revenue: "
        f"${completed_revenue:,.2f}"
    )

    print(
        f"Average order value: "
        f"${average_order_value:,.2f}"
    )


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

def main():

    print("=" * 60)
    print("END-TO-END SNOWFLAKE & DBT ANALYTICS PLATFORM")
    print("Data Ingestion & Validation")
    print("=" * 60)

    data = load_data()

    validate_schema(data)

    validate_primary_keys(data)

    missing_value_analysis(data)

    calculate_metrics(data)

    print("\nPipeline validation completed.")


if __name__ == "__main__":
    main()
