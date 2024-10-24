# Indian Weather Dashboard

## Description
The Indian Weather Dashboard is a web application that provides real-time weather information for various cities in India. It offers a user-friendly interface to select a city and view current weather conditions, including temperature, humidity, wind speed, and weather description.

## Features
- Real-time weather data for Indian cities
- Automatic updates every 5 minutes
- Responsive design for desktop and mobile devices
- Visual weather icons for easy interpretation
- Error handling for failed API requests

## Technologies Used
- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask
- API: OpenWeatherMap

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/indian-weather-dashboard.git
   cd indian-weather-dashboard
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your OpenWeatherMap API key:
   ```
   OPENWEATHERMAP_API_KEY=your_api_key_here
   ```

## Usage

1. Start the Flask server:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

3. Select a city from the dropdown menu to view its current weather information

## Project Structure

```
indian-weather-dashboard/
├── app.py
├── src/
│ ├── init.py
│ ├── config.py
│ └── weather_utils.py
├── static/
│ ├── css/
│ │ └── styles.css
│ └── js/
│ └── script.js
├── templates/
│ └── index.html
├── requirements.txt
├── .env
└── README.md
```

Note: Files and directories marked as (Optional) are not required for basic functionality but can be added for better code organization and scalability.


## Configuration
- The list of available cities can be modified in `src/config.py`
- API settings and other configurations are managed through environment variables in the `.env` file

## Contributing
Contributions to improve the Indian Weather Dashboard are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Weather data provided by [OpenWeatherMap](https://openweathermap.org/)
- Icons by [Font Awesome](https://fontawesome.com/)
