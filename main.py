from flask import Flask
import logging
from Controller.api import get_weather


logging.basicConfig(
    level=logging.DEBUG,  # Set the desired logging level
    format="%(asctime)s - %(levelname)s - %(message)s",  # Customize the format
    handlers=[logging.StreamHandler()]  # Use a StreamHandler to write to the console (optional)
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/api/weather/<city>")
def get_current_weather(city):
    #logger.debug(f"Fetching weather data for city: {city}")
    logger.info(f"Successfully retrieved weather data for city: {city}")
    return get_weather(city)


if __name__ == '__main__':
    logger.info(f"Starting API")
    app.run(debug=False)
    logger.info(f"Finish API")
