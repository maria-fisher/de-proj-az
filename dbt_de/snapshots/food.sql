{% snapshot food_snapshot %}

{{
    config(
      file_format = "delta",
      location_root = "/mnt/silver/food",
      target_schema='snapshots',
      invalidate_hard_deletes=True,
      unique_key='food_id',
      strategy='check',
      check_cols='all'
    )
}}

with source_data as (
    select
        food_id,
        food_type,
        station,
        quantity,
        price_unity,
        price_total
    from {{ source('storage', 'food') }}
)
select *
from source_data

{% endsnapshot %}
