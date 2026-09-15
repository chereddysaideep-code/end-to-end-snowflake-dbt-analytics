{{ config(materialized='view') }}

SELECT
    product_id,
    product_name,
    category,
    unit_price
FROM {{ source('raw', 'products') }}
WHERE product_id IS NOT NULL
