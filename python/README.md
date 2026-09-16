# Python Data Ingestion

This directory contains Python scripts used to validate and ingest
sample e-commerce data into Snowflake.

## Files

### `ingest.py`

Performs initial data validation before loading data into Snowflake.

Validation includes:

- File availability
- Column/schema validation
- Primary key validation
- Missing-value analysis
- Revenue calculations
- Completed-order metrics

### `snowflake_loader.py`

Loads validated CSV datasets into the Snowflake `RAW` layer.

The loader:

1. Reads CSV files using Pandas.
2. Connects to Snowflake using environment variables.
3. Loads data into RAW tables.
4. Commits the transaction after successful loading.
5. Rolls back the transaction when an error occurs.
6. Closes the Snowflake connection safely.

## Data Sources

The sample datasets include:

- Customers
- Products
- Orders
- Order Items

## Security

Snowflake credentials are stored in environment variables and are
not committed to GitHub.

Use `.env.example` as a template for local configuration.

## Technologies

- Python
- Pandas
- Snowflake Connector for Python
- Snowflake
- CSV
- Data Validation
- ETL / ELT
