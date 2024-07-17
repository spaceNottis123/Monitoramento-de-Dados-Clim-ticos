from flask import Flask, jsonify
from models.logger import get_logger
from Controller.api import get_weather
from flasgger import Swagger


app = Flask(__name__)
logger = get_logger(__name__)
swagger = Swagger(app, template_file='Documentation/swagger.yml')


@app.route("/api/weather/<city>")
def get_current_weather(city):
    logger.info(f"Successfully retrieved weather data for city: {city}")
    weather_data = get_weather(city)
    logger.info(f"Successfully retrieved weather data for city: {city}")
    return jsonify(weather_data)


if __name__ == '__main__':
    logger.info("Starting API")
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        logger.error(f"Error starting the API: {e}")
    finally:
        logger.info("Stopping API")
