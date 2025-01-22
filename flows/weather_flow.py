from prefect import task, flow
from extract import extract
from transform import transform
from load import load

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


if __name__ == "__main__":
    weather_flow.serve(
        name="Weather_Flow",
        cron="*/10 * * * *"
    )