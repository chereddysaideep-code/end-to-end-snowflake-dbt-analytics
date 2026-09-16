# Project Architecture

## End-to-End Data Flow

```text
                    DATA SOURCES
                         |
                         v
              +---------------------+
              |   CSV Sample Data   |
              +---------------------+
                         |
                         v
              +---------------------+
              | Python Validation   |
              | Pandas / Quality    |
              +---------------------+
                         |
                         v
              +---------------------+
              |   Snowflake RAW     |
              | Customers           |
              | Products            |
              | Orders              |
              | Order Items         |
              +---------------------+
                         |
                         v
              +---------------------+
              |    dbt STAGING      |
              | Cleaning & Standard |
              +---------------------+
                         |
                         v
              +---------------------+
              | dbt INTERMEDIATE    |
              | Joins & Business    |
              | Transformations     |
              +---------------------+
                         |
                         v
              +---------------------+
              |     dbt MARTS       |
              | Dimensions & Facts  |
              +---------------------+
                         |
                         v
              +---------------------+
              | BI / Analytics      |
              | Power BI / Looker   |
              +---------------------+
