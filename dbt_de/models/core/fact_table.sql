{{ 
    config(
        materialized = "table",
        file_format = "delta",
        location_root = "/mnt/gold/sensors"
    )
}}

-- Assuming that all tables have been created in the 'snapshots' schema

WITH co2_data AS (
    SELECT
        event_id,
        season,
        timestamp,
        station,
        co2_min,
        co2_max
    FROM snapshots.co2_snapshot
),
rh_data AS (
    SELECT
        event_id,
        season,
        timestamp,
        station,
        humidity_min,
        humidity_max
    FROM snapshots.rh_snapshot
),
temperature_data AS (
    SELECT
        event_id,
        season,
        timestamp,
        station,
        temperature_min,
        temperature_max
    FROM snapshots.temperature_snapshot
),
wa_data AS (
    SELECT
        event_id,
        season,
        timestamp,
        station,
        wa_min,
        wa_max
    FROM snapshots.wa_snapshot
)
SELECT
    co2_data.event_id,
    co2_data.season,
    co2_data.timestamp,
    co2_data.station,
    co2_data.co2_min,
    co2_data.co2_max,
    rh_data.humidity_min,
    rh_data.humidity_max,
    temperature_data.temperature_min,
    temperature_data.temperature_max,
    wa_data.wa_min,
    wa_data.wa_max
FROM
    co2_data
    INNER JOIN rh_data ON co2_data.event_id = rh_data.event_id
    INNER JOIN temperature_data ON co2_data.event_id = temperature_data.event_id
    INNER JOIN wa_data ON co2_data.event_id = wa_data.event_id;
