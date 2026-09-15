{{ config(materialized='table') }}

WITH date_spine AS (
    SELECT
        DATEADD(
            day,
            SEQ4(),
            '2024-01-01'::DATE
        ) AS date_day
    FROM TABLE(GENERATOR(ROWCOUNT => 731))
)

SELECT
    date_day,
    YEAR(date_day) AS year,
    MONTH(date_day) AS month,
    MONTHNAME(date_day) AS month_name,
    QUARTER(date_day) AS quarter,
    DAY(date_day) AS day,
    DAYOFWEEK(date_day) AS day_of_week,
    DAYNAME(date_day) AS day_name,
    CASE
        WHEN DAYOFWEEK(date_day) IN (1, 7) THEN FALSE
        ELSE TRUE
    END AS is_weekday
FROM date_spine
