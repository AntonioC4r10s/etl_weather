# ETL-WEATHER

Este repositório contém um projeto de Extração, Transformação e Carregamento (ETL) para dados de clima, utilizando a API do [WeatherAPI](https://www.weatherapi.com/).

## Objetivo

O objetivo do projeto é criar um pipeline ETL para coletar, processar e carregar dados de clima para uma base de dados.

## Requisitos

* Python 3.6+
* pip
* dotenv
* requests
* pandas
* prefect

## Instalação

1. Clone o repositório
2. Instale as dependências com o comando `pip install -r requirements.txt`
3. Crie um arquivo `.env` com as variáveis de ambiente necessárias:
	* `W_API_KEY`: a chave da API do WeatherAPI
	* `CITIES`: uma lista de cidades separadas por vírgula, exemplo: "paris,london,new york,tokyo,sydney"
4. Execute o comando `python run.py` para executar o pipeline ETL

## Funcionalidades

* Extração: coleta dados de clima para as cidades especificadas na variável de ambiente `CITIES`
* Transformação: processa os dados coletados e os transforma em um formato padrão
* Carregamento: carrega os dados processados em uma base de dados

## Arquitetura

O pipeline ETL é dividido em quatro etapas:

1. Extração: o script `extract.py` coleta dados de clima para as cidades especificadas na variável de ambiente `CITIES`
2. Transformação: o script `transform.py` processa os dados coletados e os transforma em um formato padrão
3. Carregamento: o script `load.py` carrega os dados processados em uma base de dados
4. Execução: o script `main.py` executa o pipeline ETL

## Desenvolvimento

O repositório contém um exemplo de notebook Jupyter para análise e visualização dos dados.

## Contribuição

Contribuições são bem-vindas! Para contribuir, basta abrir um pull request com as alterações desejadas.
