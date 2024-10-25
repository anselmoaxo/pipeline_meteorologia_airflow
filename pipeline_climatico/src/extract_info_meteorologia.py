import os
from os.path import join
from datetime import datetime, timedelta
import pandas as pd
from dotenv import load_dotenv



# Carregar o .env
load_dotenv()

# Acessar as variáveis de ambiente
key = os.getenv('API_KEY')

# intervalso de data (inicio / final)
data_inicio = datetime.today()
data_final = data_inicio + timedelta(days=7)

# converter formato
data_inicio = data_inicio.strftime('%Y-%m-%d')
data_final = data_final.strftime('%Y-%m-%d')

city = 'Guarulhos'
key = key


# Api para Extrai os dados do Clima
URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
            f'{city}/{data_inicio}/{data_final}?unitGroup=metric&include=days&key={key}&contentType=csv')

#criando o DataFrame
dados_clima = pd.read_csv(URL)

file_path = f'/home/anselmo/airflow_meteorologia/datalake/bronze/semana={data_inicio}/'
# criando diretorio com os.mkdir
os.makedirs(file_path, exist_ok=True)

# Salvar dentro do Datalake/Bronze
dados_clima.to_csv(file_path + 'dados_brutos.csv')
dados_clima[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv')
dados_clima[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')


