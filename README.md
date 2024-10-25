# Projeto de Pipeline de Dados Meteorológicos

## Descrição

Este projeto implementa um pipeline de dados meteorológicos, que coleta previsões de 7 dias para uma determinada localidade, armazenando-as em um datalake local. O pipeline é agendado para execução automática toda segunda-feira, utilizando o Apache Airflow para orquestração.

## Objetivo

Automatizar a coleta e armazenamento de dados meteorológicos, criando uma fonte de dados consistente para análises climáticas e previsões. Este pipeline oferece flexibilidade para expandir e adaptar o processo, integrando facilmente novos destinos de armazenamento e visualização de dados.

## Estrutura do Projeto

O pipeline está organizado nas seguintes etapas:

1. **Extração dos Dados**: Realizada por meio de uma API meteorológica, capturando previsões de 7 dias.
2. **Armazenamento no Datalake**: Os dados extraídos são salvos em um diretório local estruturado, facilitando o controle e manipulação posterior.
3. **Orquestração com Airflow**: O Airflow é utilizado para automatizar e agendar o fluxo, executando-o toda segunda-feira e monitorando possíveis falhas.

## Tecnologias Utilizadas

- **Python**: Para desenvolver os scripts de extração e processamento de dados.
- **Apache Airflow**: Orquestração e agendamento das tarefas.
- **API de Meteorologia**: Fonte de dados .
- **Datalake Local**: Diretório estruturado para armazenamento de dados extraídos.

## Requisitos

- Python 3.8 ou superior
- Apache Airflow (v2.3.2 ou superior recomendada)
- Dependências adicionais listadas em `requirements.txt`

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/anselmoaxo/pipeline_meteorologia_airflow
   


## Contribuições
Contribuições são bem-vindas! Por favor, crie um fork deste repositório e envie um pull request com melhorias, correções ou novas funcionalidades.



