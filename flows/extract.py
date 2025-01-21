from dotenv import load_dotenv
import os
import requests


load_dotenv()
api_key = os.getenv("W_API_KEY")
cities = ["paris", "london", "new york", "tokyo", "sydney"]
base_URL = "http://api.weatherapi.com/v1"


def extract():
    """
    Extract the current weather data from the Weather API for the given cities

    For each city, the current weather data is retrieved from the Weather API
    and the JSON response is written to a CSV file with the city name.
    """
    datas = []
    for city in cities:
        url = f"{base_URL}/current.json?key={api_key}&q={city}"
        response = requests.get(url)
        data = response.json()
        datas.append(data)
        with open(f"data/raw/{city}.txt", "a") as f:
            f.write(f"{data}\n")


if __name__ == "__main__":
    extract()