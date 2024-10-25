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


def extrai_dados(data_inicio, data_final):
    
    city = 'Guarulhos'
    key = carrega_dados()

    # Construir a URL da API
    URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
                f'{city}/{data_inicio}/{data_final}?unitGroup=metric&include=days&key={key}&contentType=csv')

    # Ler os dados da API
    dados_clima = pd.read_csv(URL)
    return dados_clima


def salva_dados_bruto(file_path, data_inicio, data_final):
    # Criar o diretório, se não existir
    os.makedirs(file_path, exist_ok=True)
    
    # Extrair os dados e salvar
    dados_clima = extrai_dados(data_inicio, data_final)
    dados_clima.to_csv(os.path.join(file_path, 'dados_brutos.csv'), index=False)



def transforma_dados(file_path_bronze, file_path_silver):
    # Ler os dados brutos
    dados_clima = pd.read_csv(join(file_path_bronze, 'dados_brutos.csv'))

    # Criar o diretório de saída, se não existir
    os.makedirs(file_path_silver, exist_ok=True)
    
    # Salvar os arquivos específicos de temperatura e condições
    dados_clima[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(join(file_path_silver, 'temperaturas.csv'), index=False)
    dados_clima[['datetime', 'description', 'icon']].to_csv(join(file_path_silver, 'condicoes.csv'), index=False)

    
    