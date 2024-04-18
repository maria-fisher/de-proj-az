{% snapshot rh_snapshot %}

{{
    config(
      file_format = "delta",
      location_root = "/mnt/silver/rh",
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
	    humidity_min,
	    humidity_max
    from {{ source('sensor', 'rh') }}
)
select *
from source_data

{% endsnapshot %}