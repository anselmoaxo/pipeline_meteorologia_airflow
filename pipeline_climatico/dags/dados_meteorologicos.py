
import sys
sys.path.append("pipeline_climatico")
from airflow.models import DAG
import pendulum
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.macros import ds_add
from src.extrai_dados_climatico import extrai_dados

with DAG(
    "Dados_Meteorologicos",
    start_date=pendulum.datetime(2024, 9, 30 ,tz="UTC"),
    schedule_interval='0 0 * * 1', #executar toda a segunda feira
)as dag:
    
    tarefa_1 = BashOperator(
        task_id = 'cria_pasta',
        bash_command = 'mkdir -p "/home/anselmo/airflow_meteorologia/datalake/bronze/semana={{data_interval_end.strftime("%Y-%m-%d")}}"'
        )
    
    tarefa_2 = PythonOperator(
        task_id='extrair_dados_climaticos',
        python_callable=extrai_dados,
        op_kwargs={
            'data_inicio': '{{ data_interval_start.strftime("%Y-%m-%d") }}',
            'data_final': '{{ data_interval_end.strftime("%Y-%m-%d") }}',
            'file_path': '/home/anselmo/airflow_meteorologia/datalake/bronze/semana={{ data_interval_end.strftime("%Y-%m-%d") }}/'
        }
    )

    # Definir a ordem de execução
    tarefa_1 >> tarefa_2
        
        
    
        
    
    