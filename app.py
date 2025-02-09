import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).resolve().parent
sys.path.append(str(project_root))

from flask import Flask, render_template, request, jsonify
from src.weather_utils import get_weather_data
from src.config import CITIES, API_KEY

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', cities=CITIES)

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    try:
        weather_data = get_weather_data(city)
        return jsonify(weather_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
