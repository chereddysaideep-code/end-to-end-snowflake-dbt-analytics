# SQL Database Layer

This directory contains SQL scripts used to create and validate the
Snowflake database environment for the analytics platform.

## `database_setup.sql`

Creates the core Snowflake database structures:

- `ANALYTICS_DB` database
- `RAW` schema
- `STAGING` schema
- `ANALYTICS` schema
- Customers table
- Products table
- Orders table
- Order Items table

## Data Validation

The SQL scripts include validation queries for:

- Row counts
- Duplicate primary keys
- NULL values
- Order revenue calculations

## Data Architecture

```text
ANALYTICS_DB
│
├── RAW
│   ├── CUSTOMERS
│   ├── PRODUCTS
│   ├── ORDERS
│   └── ORDER_ITEMS
│
├── STAGING
│
└── ANALYTICS
