{% snapshot wa_snapshot %}

{{
    config(
      file_format = "delta",
      location_root = "/mnt/silver/wa",
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
	    wa_min,
	    wa_max
    from {{ source('sensor', 'wa') }}
)
select *
from source_data

{% endsnapshot %}