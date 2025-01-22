from .extract import cities
import json

def transform():

    """
    Transforms raw weather data files into a list of dictionaries with processed information.

    This function reads the latest weather data for each city from text files, 
    processes the JSON data, and extracts relevant weather information. The processed 
    data is stored in a list of dictionaries, each containing details such as 
    name, region, country, temperature, weather condition, wind information, 
    pressure, humidity, cloud coverage, UV index, and more.

    Returns:
        list: A list of dictionaries containing processed weather data for each city.
    """

    json_cities_processed = []
    for city in cities:
        with open(f"data/raw/{city}.txt", "r") as f:
            data = f.read().splitlines()
            data = data[len(data)-1]
            data = data.replace("'", '"')
            data = json.loads(data)

            name = data["location"]["name"]
            region = data["location"]["region"]
            country = data["location"]["country"]
            temp_c = data["current"]["temp_c"]
            temp_f = data["current"]["temp_f"]
            is_day = data["current"]["is_day"]
            condition = data["current"]["condition"]["text"]
            wind_mph = data["current"]["wind_mph"]
            wind_kph = data["current"]["wind_kph"]
            wind_degree = data["current"]["wind_degree"]
            wind_dir = data["current"]["wind_dir"]
            pressure_mb = data["current"]["pressure_mb"]
            pressure_in = data["current"]["pressure_in"]
            precip_mm = data["current"]["precip_mm"]
            humidity = data["current"]["humidity"]
            cloud = data["current"]["cloud"]
            uv = data["current"]["uv"]
            gust_mph = data["current"]["gust_mph"]
            gust_kph = data["current"]["gust_kph"]
            condition = data["current"]["condition"]["text"]
            icon = data["current"]["condition"]["icon"]
            code = data["current"]["condition"]["code"]
            vis_km = data["current"]["vis_km"]
            vis_miles = data["current"]["vis_miles"]
            feelslike_c = data["current"]["feelslike_c"]
            feelslike_f = data["current"]["feelslike_f"]
            windchill_c = data["current"]["windchill_c"]
            windchill_f = data["current"]["windchill_f"]
            heatindex_c = data["current"]["heatindex_c"]
            heatindex_f = data["current"]["heatindex_f"]
            dewpoint_c = data["current"]["dewpoint_c"]
            dewpoint_f = data["current"]["dewpoint_f"]

            json_cities_processed.append(
                {
                "name": name,
                "region": region,
                "country": country,
                "temp_c": temp_c,
                "temp_f": temp_f,
                "is_day": is_day,
                "condition": condition,
                "wind_mph": wind_mph,
                "wind_kph": wind_kph,
                "wind_degree": wind_degree,
                "wind_dir": wind_dir,
                "pressure_mb": pressure_mb,
                "pressure_in": pressure_in,
                "precip_mm": precip_mm,
                "humidity": humidity,
                "cloud": cloud,
                "uv": uv,
                "gust_mph": gust_mph,
                "gust_kph": gust_kph,
                "condition": condition,
                "icon": icon,
                "code": code,
                "vis_km": vis_km,
                "vis_miles": vis_miles,
                "feelslike_c": feelslike_c,
                "feelslike_f": feelslike_f,
                "windchill_c": windchill_c,
                "windchill_f": windchill_f,
                "heatindex_c": heatindex_c,
                "heatindex_f": heatindex_f,
                "dewpoint_c": dewpoint_c,
                "dewpoint_f": dewpoint_f
            }
            )
    return json_cities_processed


if __name__ == "__main__":
    data = transform()
    print(data)