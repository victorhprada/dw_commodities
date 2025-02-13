-- importando a tabela movimentacao_commodities

with source_movimentacao_commodities as (
    select
        date,
        symbol,
        action,
        quantity
    from {{ source('dbcommodities_a6yp', 'movimentacao_commodities') }}
),

-- renamed

renamed as (
    select
        cast(date as date) as data,
        "symbol" as simbolo,
        "action" as acao,
        "quantity" as quantidade
    from source_movimentacao_commodities
)

-- selecionando as colunas

select * from renamed