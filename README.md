# End-to-End Snowflake & dbt Analytics Platform

An end-to-end analytics engineering project demonstrating data ingestion,
validation, cloud data warehousing, transformation, data quality testing,
dimensional modeling, and business intelligence.

## Project Overview

This project demonstrates a complete data workflow from raw sample data
through Python-based validation and Snowflake ingestion, followed by dbt
transformations and analytics-ready data models.

The project uses synthetic e-commerce data for demonstration purposes.

## Architecture

```text
CSV Sample Data
      |
      v
Python / Pandas
Data Validation
      |
      v
Snowflake RAW
      |
      v
dbt STAGING
      |
      v
dbt INTERMEDIATE
      |
      v
dbt MARTS
      |
      v
Power BI / Looker
