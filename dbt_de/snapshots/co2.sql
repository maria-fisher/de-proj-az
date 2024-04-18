{% snapshot co2_snapshot %}

{{
    config(
      file_format = "delta",
      location_root = "/mnt/silver/co2",
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
	    co2_min,
	    co2_max
    from {{ source('sensor', 'co2') }}
)
select *
from source_data

{% endsnapshot %}