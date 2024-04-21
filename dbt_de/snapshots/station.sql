{% snapshot station_snapshot %}

{{
    config(
      file_format = "delta",
      location_root = "/mnt/silver/station",
      target_schema='snapshots',
      invalidate_hard_deletes=True,
      unique_key='station',
      strategy='check',
      check_cols='all'
    )
}}

with source_data as (
    select
        station,
        food_type
    from {{ source('storage', 'station') }}
)
select *
from source_data

{% endsnapshot %}
