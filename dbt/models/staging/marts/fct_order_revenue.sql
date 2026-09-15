{{ config(materialized='table') }}

SELECT
    order_id,
    customer_id,
    order_date,
    SUM(item_revenue) AS order_revenue,
    COUNT(DISTINCT order_item_id) AS item_count,
    SUM(quantity) AS total_quantity
FROM {{ ref('int_order_items_enriched') }}
WHERE order_status = 'Completed'
GROUP BY
    order_id,
    customer_id,
    order_date
