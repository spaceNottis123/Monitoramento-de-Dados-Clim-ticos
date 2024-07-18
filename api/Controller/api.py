from flask import jsonify
from models.weather import WeatherData
from utils.openweathermap_api import fetch_weather_data, geolocation
from models.logger import get_logger

logger = get_logger(__name__)


def get_weather(city):
    logger.info(f"Fetching weather data for city: {city}")
    try:
        data = fetch_weather_data(city)
        if not data:
            logger.error(f"Error retrieving weather data for city: {city}")
            return jsonify({"error": "Error retrieving weather data"}), 500

        if 'weather' not in data:
            logger.warning(f"Weather data not available for city: {city}")
            return jsonify({"error": "Weather data not available"}), 404

        description = [i['description'] for i in data['weather']]
        format_desc = str(description).replace("['", "").replace("']", "")

        geolocationcountry = geolocation(city)

        weather = WeatherData(city, data['main']['temp'], data['main']['temp_min'], data['main']['temp_max'],
                              data['main']['feels_like'], format_desc, geolocationcountry["country"])
        json_response = {
            "city": weather.city,
            "description": weather.description,
            "temperature": weather.temp,
            "temperature max": weather.temp_max,
            "temperature min": weather.temp_min,
            "feels_like": weather.feels_like,
            "country": weather.country
        }
        logger.info(f"Successfully retrieved weather data for city: {city}")
        logger.info(f"message: {json_response}")
        return json_response
    except Exception as e:
        logger.error(f"Exception occurred while fetching weather data for city: {city}, Error: {e}")
        return jsonify({"error": "Internal server error"}), 500
