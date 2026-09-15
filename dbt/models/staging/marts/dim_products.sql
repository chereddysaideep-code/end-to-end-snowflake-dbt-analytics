{{ config(materialized='table') }}

SELECT
    product_id,
    product_name,
    category,
    unit_price
FROM {{ ref('stg_products') }}
WHERE product_id IS NOT NULL
