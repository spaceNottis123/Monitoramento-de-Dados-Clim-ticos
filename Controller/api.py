from models.weather import WeatherData
from utils.openweathermap_api import fetch_weather_data


def get_weather():
    data = fetch_weather_data()
    print(type(data))
    weather = WeatherData(data["temp"], data["temperature_min"], data["temperature_max"], data["feels_like"] )
    return weather


print(get_weather())
