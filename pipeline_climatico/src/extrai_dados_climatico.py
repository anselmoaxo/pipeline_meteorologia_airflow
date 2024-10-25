import os
from os.path import join
import pandas as pd
from dotenv import load_dotenv


def carrega_dados():
    
    load_dotenv(dotenv_path='/home/anselmo/airflow_meteorologia/.env')
    key = os.getenv('API_KEY')
    if key is None:
        raise ValueError("API_KEY não encontrada. Verifique o arquivo .env.")
    return key


def extrai_dados(data_inicio, data_final, file_path):
    # Criar o diretório, se não existir
    os.makedirs(file_path, exist_ok=True)
    
    city = 'Guarulhos'
    key = carrega_dados()

    # Construir a URL da API
    URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
                f'{city}/{data_inicio}/{data_final}?unitGroup=metric&include=days&key={key}&contentType=csv')

    # Ler os dados da API
    dados_clima = pd.read_csv(URL)

    # Salvar os arquivos no diretório especificado
    dados_clima.to_csv(file_path + 'dados_brutos.csv', index=False)
    dados_clima[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv', index=False)
    dados_clima[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv', index=False)
