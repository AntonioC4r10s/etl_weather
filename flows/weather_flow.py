from prefect import task, flow
from flows.extract import extract
from flows.transform import transform
from flows.load import load

@task
def extract_data():
    extract()
    print("Data extracted")

@task
def transform_data():
    data = transform()
    print("Data transformed")
    return data

@task
def load_data(data):
    print("Data loaded")
    load(data)

@flow
def weather_flow():
    extract_data()
    data = transform_data()
    load_data(data)
