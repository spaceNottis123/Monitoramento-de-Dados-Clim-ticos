from flask import Flask, jsonify
from models.weather import WeatherData
from utils.openweathermap_api import fetch_weather_data


def get_weather(city):
    data = fetch_weather_data(city)
    description = [i['description'] for i in data['weather']]
    format_desc = str(description).replace("['", "").replace("']", "")
    weather = WeatherData(city, data['main']['temp'], data['main']['temp_min'], data['main']['temp_max'],
                          data['main']['feels_like'], format_desc)
    json_response = {
        "city": weather.city,
        "description": weather.description,
        "temperature": weather.temp,
        "temperature max": weather.temp_max,
        "temperature min": weather.temp_min,
        "feels_like": weather.feels_like

    }

    return jsonify(json_response)

