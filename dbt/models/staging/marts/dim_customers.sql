{{ config(materialized='table') }}

SELECT
    customer_id,
    customer_name,
    email,
    country,
    signup_date
FROM {{ ref('stg_customers') }}
WHERE customer_id IS NOT NULL
