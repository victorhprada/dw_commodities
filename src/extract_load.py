import yfinance as yf
import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Importando as variaveis de ambiente
commodities = ['CL=F', 'GC=F', 'SI=F', 'HG=F', 'PL=F', 'ZM=F', 'ZC=F', 'ZS=F', 'ZM=F', 'ZC=F', 'ZS=F']

# Carregando as variáveis de ambiente
load_dotenv()

# Criando a conexão com o banco de dados
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')

# Criando string de conexão e engine
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
engine = create_engine(DATABASE_URL)

def search_commodities_data(simbolo, periodo='30d', intervalo='1d'):
    ticker = yf.Ticker(simbolo)
    dados = ticker.history(period=periodo, interval=intervalo)[['Close']]
    dados['simbolo'] = simbolo
    return dados

def search_all_commodities_data():
    all_data = []
    for simbolo in commodities:
        dados = search_commodities_data(simbolo)
        all_data.append(dados)
    return pd.concat(all_data)

def save_data_to_postgres(df, schema='public'):
    df.to_sql('commodities', engine, schema=schema, if_exists='replace', index=True)

if __name__ == '__main__':
    concat_data = search_all_commodities_data()
    save_data_to_postgres(concat_data, schema='public')