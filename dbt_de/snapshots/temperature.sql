{% snapshot temperature_snapshot %}

{{
    config(
      file_format = "delta",
      location_root = "/mnt/silver/temperature",
      target_schema='snapshots',
      invalidate_hard_deletes=True,
      unique_key='event_id',
      strategy='check',
      check_cols='all'
    )
}}

with source_data as (
    select
        event_id ,
	    season,
	    timestamp,
	    station,
	    temperature_min,
	    temperature_max
    from {{ source('sensor', 'temperature') }}
)
select *
from source_data

{% endsnapshot %}