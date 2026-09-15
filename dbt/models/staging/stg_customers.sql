{{ config(materialized='view') }}

SELECT
    customer_id,
    customer_name,
    email,
    country,
    signup_date
FROM {{ source('raw', 'customers') }}
WHERE customer_id IS NOT NULL
