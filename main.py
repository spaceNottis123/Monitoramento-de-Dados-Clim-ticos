from flask import Flask, jsonify
import logging
from logging.handlers import RotatingFileHandler
from Controller.api import get_weather

app = Flask(__name__)

print("Setting up logging...")

if not app.debug:
    handler = RotatingFileHandler('api.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    # Set the logger level to INFO
    app.logger.setLevel(logging.INFO)
    print("Logging set up completed")


@app.route("/api/weather/<city>")
def get_current_weather(city):
    app.logger.info(f"Successfully retrieved weather data for city: {city}")
    try:
        weather_data = get_weather(city)
        app.logger.info(f"Successfully retrieved weather data for city: {city}")
        return jsonify(weather_data)
    except Exception as e:
        app.logger.error(f"Error retrieving weather data for city: {city}. Error: {e}")
        return jsonify({"error": "Unable to retrieve weather data"}), 500

if __name__ == '__main__':
    app.logger.info("Starting API")
    try:
        app.run(debug=False)
    except Exception as e:
        app.logger.error(f"Error starting the API: {e}")
    finally:
        app.logger.info("Stopping API")

