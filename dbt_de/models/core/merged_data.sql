{{ 
    config(
        materialized = "table",
        file_format = "delta",
        location_root = "/mnt/gold/storage"
    )
}}

WITH food_data AS (
    SELECT
        food_id,
        food_type,
        station,
        quantity,
        price_unity,
        price_total
    FROM snapshots.food_snapshot
),
sensors_data AS (
    SELECT
        event_id,
        temp,
        rh,
        co2,
        wa,
        station,
        datetime
    FROM snapshots.sensors_snapshot
),
station_data AS (
    SELECT
        station,
        food_type
    FROM snapshots.station_snapshot
)
SELECT
    sensors.event_id,
    sensors.temp,
    sensors.rh,
    sensors.co2,
    sensors.wa,
    sensors.station,
    sensors.datetime,
    food.quantity,
    food.price_unity,
    food.price_total,
    station.food_type AS station_food_type
FROM
    sensors_data sensors
LEFT JOIN
    food_data food
ON
    sensors.station = food.station
LEFT JOIN
    station_data station
ON
    sensors.station = station.station;
