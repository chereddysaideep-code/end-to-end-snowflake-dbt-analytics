{{ config(materialized='view') }}

SELECT
    order_item_id,
    order_id,
    product_id,
    quantity,
    unit_price
FROM {{ source('raw', 'order_items') }}
WHERE order_item_id IS NOT NULL
