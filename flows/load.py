import pandas as pd
import os
from .transform import transform

def load(data: list) -> None:
    
    """
    Save the processed data to CSV files in the "data/processed" directory.

    The data is saved as one CSV file per city, with each row representing a single
    measurement. The columns of the CSV file are the same as the keys in the 
    dictionaries in the input list.

    If the file does not exist, it is created. If it does exist, the new data is 
    appended to the end of the file.
    """
    for city_data in data:
        city = city_data["name"]
        path = f"data/processed/{city}.csv"
        record = {
            "name": city_data["name"],
            "region": city_data["region"],
            "country": city_data["country"],
            "temp_c": city_data["temp_c"],
            "temp_f": city_data["temp_f"],
            "is_day": city_data["is_day"],
            "condition": city_data["condition"],
            "wind_mph": city_data["wind_mph"],
            "wind_kph": city_data["wind_kph"],
            "wind_degree": city_data["wind_degree"],
            "wind_dir": city_data["wind_dir"],
            "pressure_mb": city_data["pressure_mb"],
            "pressure_in": city_data["pressure_in"],
            "precip_mm": city_data["precip_mm"],
            "humidity": city_data["humidity"],
            "cloud": city_data["cloud"],
            "uv": city_data["uv"],
            "gust_mph": city_data["gust_mph"],
            "gust_kph": city_data["gust_kph"],
            "icon": city_data["icon"],
            "code": city_data["code"],
            "vis_km": city_data["vis_km"],
            "vis_miles": city_data["vis_miles"],
            "feelslike_c": city_data["feelslike_c"],
            "feelslike_f": city_data["feelslike_f"],
            "windchill_c": city_data["windchill_c"],
            "windchill_f": city_data["windchill_f"],
            "heatindex_c": city_data["heatindex_c"],
            "heatindex_f": city_data["heatindex_f"],
            "dewpoint_c": city_data["dewpoint_c"],
            "dewpoint_f": city_data["dewpoint_f"],
        }
        if not os.path.exists(path):
            pd.DataFrame([record]).to_csv(path, index=False)
        else:
            pd.DataFrame([record]).to_csv(path, mode='a', header=False, index=False)


if __name__ == "__main__":
    data = transform()
    print(data)
    load(data)