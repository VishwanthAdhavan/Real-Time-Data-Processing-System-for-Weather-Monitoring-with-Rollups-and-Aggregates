from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)
app.config['SESSION_COOKIE_SECURE'] = False
app.config['WTF_CSRF_ENABLED'] = False

@app.route('/')
def index():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Indian Weather Dashboard</title>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Roboto', sans-serif;
                background: linear-gradient(135deg, #00b4db, #0083b0);
                margin: 0;
                padding: 0;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }
            .container {
                background-color: rgba(255, 255, 255, 0.9);
                border-radius: 20px;
                padding: 30px;
                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
                max-width: 400px;
                width: 100%;
            }
            h1 {
                color: #333;
                text-align: center;
                margin-bottom: 30px;
            }
            select {
                width: 100%;
                padding: 12px;
                border: 1px solid #ddd;
                border-radius: 5px;
                font-size: 16px;
                margin-bottom: 20px;
            }
            #weather-info {
                background-color: #f8f9fa;
                border-radius: 10px;
                padding: 20px;
                margin-top: 20px;
                text-align: center;
            }
            #weather-info h2 {
                color: #0083b0;
                margin-bottom: 15px;
            }
            .weather-detail {
                display: flex;
                justify-content: space-between;
                margin-bottom: 10px;
            }
            .weather-detail span:first-child {
                font-weight: bold;
                color: #555;
            }
            #loading {
                text-align: center;
                color: #666;
            }
            .error {
                color: #d9534f;
                text-align: center;
            }
            #last-updated {
                text-align: center;
                font-size: 0.8em;
                color: #666;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Indian Weather Dashboard</h1>
            <select id="city-select">
                <option value="">Choose a city</option>
                <option value="Mumbai">Mumbai</option>
                <option value="Delhi">Delhi</option>
                <option value="Bangalore">Bangalore</option>
                <option value="Kolkata">Kolkata</option>
                <option value="Chennai">Chennai</option>
            </select>
            <div id="loading" style="display: none;">Fetching weather data...</div>
            <div id="weather-info"></div>
            <div id="last-updated"></div>
        </div>
        <script>
            let currentCity = '';
            let updateInterval;

            function updateLastUpdated() {
                const now = new Date();
                document.getElementById('last-updated').textContent = `Last updated: ${now.toLocaleTimeString()}`;
            }

            function fetchWeatherData(city) {
                const weatherInfo = document.getElementById('weather-info');
                const loading = document.getElementById('loading');

                loading.style.display = 'block';
                weatherInfo.innerHTML = '';

                fetch('/get_weather', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                    body: 'city=' + encodeURIComponent(city)
                })
                .then(response => response.json())
                .then(data => {
                    loading.style.display = 'none';
                    if (data.error) {
                        weatherInfo.innerHTML = `<p class="error">Error: ${data.error}</p>`;
                    } else {
                        weatherInfo.innerHTML = `
                            <h2>${data.city}</h2>
                            <div class="weather-detail">
                                <span>Temperature:</span>
                                <span>${data.temperature}°C</span>
                            </div>
                            <div class="weather-detail">
                                <span>Description:</span>
                                <span>${data.description}</span>
                            </div>
                            <div class="weather-detail">
                                <span>Humidity:</span>
                                <span>${data.humidity}%</span>
                            </div>
                            <div class="weather-detail">
                                <span>Wind Speed:</span>
                                <span>${data.wind_speed} m/s</span>
                            </div>
                        `;
                        updateLastUpdated();
                    }
                })
                .catch(error => {
                    loading.style.display = 'none';
                    weatherInfo.innerHTML = `<p class="error">Error: ${error.message}</p>`;
                });
            }

            function startAutoUpdate() {
                if (updateInterval) {
                    clearInterval(updateInterval);
                }
                updateInterval = setInterval(() => {
                    if (currentCity) {
                        fetchWeatherData(currentCity);
                    }
                }, 5 * 60 * 1000); // 5 minutes in milliseconds
            }

            document.getElementById('city-select').addEventListener('change', function() {
                currentCity = this.value;
                if (currentCity) {
                    fetchWeatherData(currentCity);
                    startAutoUpdate();
                } else {
                    document.getElementById('weather-info').innerHTML = '';
                    document.getElementById('last-updated').textContent = '';
                    if (updateInterval) {
                        clearInterval(updateInterval);
                    }
                }
            });
        </script>
    </body>
    </html>
    """)

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    # Your weather data fetching logic here
    weather_data = {
        "city": city,
        "temperature": 25,
        "description": "Sunny",
        "humidity": 60,
        "wind_speed": 5.5
    }
    response = jsonify(weather_data)
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

if __name__ == '__main__':
    app.run(debug=True)
