from flask import jsonify
from models.weather import WeatherData
from utils.openweathermap_api import fetch_weather_data, geolocation


def get_weather(city):
    data = fetch_weather_data(city)
    if not data:
        return jsonify({"error": "Error retrieving weather data"}), 500

    if 'weather' not in data:
        return jsonify({"error": "Weather data not available"}), 404

    description = [i['description'] for i in data['weather']]
    format_desc = str(description).replace("['", "").replace("']", "")

    geolocationCountry = geolocation(city)

    weather = WeatherData(city, data['main']['temp'], data['main']['temp_min'], data['main']['temp_max'],
                          data['main']['feels_like'], format_desc, geolocationCountry["country"])
    json_response = {
        "city": weather.city,
        "description": weather.description,
        "temperature": weather.temp,
        "temperature max": weather.temp_max,
        "temperature min": weather.temp_min,
        "feels_like": weather.feels_like,
        "country": weather.country
    }

    return jsonify(json_response)
