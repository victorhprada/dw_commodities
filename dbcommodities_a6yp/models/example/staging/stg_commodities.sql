-- importando a tabela commodities

with source_commodities as (
    select
        "Date",
        "Close",
        "simbolo"
    from "dbcommodities_a6yp"."public"."commodities"
),

-- renamed

renamed as (
    select
        cast("Date" as date) as data,
        cast("Close" as float) as valor_fechamento,
        "simbolo" as simbolo
    from source_commodities
)

-- selecionando as colunas

select * from renamed