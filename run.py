from flows.weather_flow import weather_flow

if __name__ == "__main__":
    weather_flow.serve(
        name="Weather_Flow",
        cron="*/10 * * * *"
    )