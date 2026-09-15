# dbt Analytics Layer

This directory contains the dbt transformation layer for the End-to-End Snowflake & dbt Analytics Platform.

## Architecture

Snowflake RAW
      |
      v
   STAGING
      |
      v
 INTERMEDIATE
      |
      v
    MARTS

## Staging Models

- `stg_customers.sql` - Cleans customer records.
- `stg_products.sql` - Cleans product records.
- `stg_orders.sql` - Cleans order records.
- `stg_order_items.sql` - Cleans order line-item records.

## Intermediate Model

### `int_order_items_enriched.sql`

Joins orders, products, and order items to create an enriched order-item dataset.

Business calculation:

`item_revenue = quantity × unit_price`

## Mart Models

### `fct_order_revenue.sql`

Creates a completed-order revenue fact table.

Key metrics:

- Order revenue
- Item count
- Total quantity

### `dim_customers.sql`

Customer dimension used for analytics and reporting.

### `dim_products.sql`

Product dimension containing product and category attributes.

### `dim_date.sql`

Calendar/date dimension used for time-based analysis.

## Data Quality

The project includes dbt tests for:

- `not_null`
- `unique`

Tests are applied to important primary-key and business-critical columns.

## Technologies

- dbt
- Snowflake
- SQL
- Dimensional Modeling
- Data Quality Testing
- ELT
- Analytics Engineering
