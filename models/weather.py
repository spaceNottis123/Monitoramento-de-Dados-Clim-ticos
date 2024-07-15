class WeatherData:
    def __init__(self, city, temperature, temperature_min, temperature_max, feels_like, description, country):
        self.city = city
        self.temp = temperature
        self.temp_min = temperature_min
        self.temp_max = temperature_max
        self.feels_like = feels_like
        self.description = description
        self.country = country
