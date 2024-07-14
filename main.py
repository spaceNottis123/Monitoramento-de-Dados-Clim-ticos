from flask import Flask

from Controller.api import get_weather

app = Flask(__name__)

@app.route("/api/weather/<city>")
def get_current_weather(city):
    return get_weather(city)


if __name__ == '__main__':
    app.run(debug=True)
