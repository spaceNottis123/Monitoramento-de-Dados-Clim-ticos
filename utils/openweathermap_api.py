import json
import requests


# Get the geolocation -- asks the city -- retrive lat, lon
def geolocation(city, api_key="904539b607db7cdc6ba7072dbd5209fb"):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"

    payload = {}
    headers = {}

    response = requests.get(url, headers=headers, data=payload).text

    data = json.loads(response)

    weather_info = {
        "lat": data[0]["lat"],
        "lon": data[0]["lon"]
    }
    return weather_info


def fetch_weather_data(api_key="904539b607db7cdc6ba7072dbd5209fb"):
    geolocation_data = geolocation(city="Sao Paulo")

    lat = geolocation_data["lat"]
    lon = geolocation_data["lon"]

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    payload = {}
    headers = {}
    response = requests.get(url, headers=headers, data=payload)
    return response.json()