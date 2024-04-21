{% snapshot sensors_snapshot %}

{{
    config(
      file_format = "delta",
      location_root = "/mnt/silver/sensors",
      target_schema='snapshots',
      invalidate_hard_deletes=True,
      unique_key='event_id',
      strategy='check',
      check_cols='all'
    )
}}

with source_data as (
    select
        event_id,
        temp,
        rh,
        co2,
        wa,
        station,
        datetime
    from {{ source('storage', 'sensors') }}
)
select *
from source_data

{% endsnapshot %}
