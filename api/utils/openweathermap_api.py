import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')
def geolocation(city):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"

    payload = {}
    headers = {}

    response = requests.get(url, headers=headers, data=payload).text

    data = json.loads(response)

    weather_info = {
        "lat": data[0]["lat"],
        "lon": data[0]["lon"],
        "country": data[0]["country"]
    }
    return weather_info


def fetch_weather_data(city):
    geolocation_data = geolocation(city)

    lat = geolocation_data["lat"]
    lon = geolocation_data["lon"]

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    payload = {}
    headers = {}
    response = requests.get(url, headers=headers, data=payload)
    return response.json()
