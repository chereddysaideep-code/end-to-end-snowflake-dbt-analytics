# BI Analytics Dashboard

This directory contains documentation and supporting materials for the
business intelligence layer of the analytics platform.

## Dashboard Purpose

The dashboard is designed to provide visibility into:

- Revenue performance
- Order trends
- Customer activity
- Product performance
- Category performance
- Average order value

## Data Source

The dashboard consumes analytics-ready data produced by the dbt
transformation layer.

Primary models include:

- `fct_order_revenue`
- `dim_customers`
- `dim_products`
- `dim_date`

## Key Metrics

- Total Revenue
- Total Orders
- Average Order Value
- Total Quantity
- Revenue by Category
- Revenue by Product
- Revenue by Month
- Customer Order Activity

## BI Tools

- Power BI
- Looker
- SQL
- Snowflake

## Reporting Flow

```text
Snowflake
    |
    v
dbt Analytics Marts
    |
    v
BI Semantic Layer
    |
    v
Power BI / Looker
    |
    v
Business Insights
