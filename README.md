# Indian Weather Dashboard

## Description
Indian Weather Dashboard is a simple, user-friendly web application that provides real-time weather information for major cities in India. Built with Flask and powered by OpenWeatherMap API, this dashboard offers current temperature, humidity, wind speed, and weather descriptions for selected Indian cities.

## Features
- Real-time weather data for major Indian cities
- User-friendly interface with a dropdown menu for city selection
- Displays temperature, humidity, wind speed, and weather description
- Auto-updates weather data every 5 minutes
- Responsive design suitable for both desktop and mobile devices

## File Structure
```
indian-weather-dashboard/
│
├── app.py                 # Main Flask application file
├── .env                   # Environment variables (API keys)
├── requirements.txt       # Python dependencies
├── .gitignore             # Git ignore file
├── README.md              # Project documentation
│
├── templates/             # (Optional) HTML templates
│   └── index.html         # Main page template
│
├── static/                # (Optional) Static files
│   ├── css/
│   │   └── styles.css     # Custom CSS styles
│   └── js/
│       └── script.js      # Custom JavaScript
│
├── weather_utils.py       # (Optional) Utility functions for weather data
└── config.py              # (Optional) Configuration settings
```

Note: Files and directories marked as (Optional) are not required for basic functionality but can be added for better code organization and scalability.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/indian-weather-dashboard.git
   cd indian-weather-dashboard
   ```

2. Create a virtual environment and activate it:
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

1. Run the Flask application:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

3. Select a city from the dropdown menu to view its current weather information

## Technologies Used
- Python
- Flask
- Flask-WTF (for CSRF protection)
- HTML/CSS
- JavaScript
- OpenWeatherMap API

## Implementation Details
- Flask is used as the web framework to handle routing and serve the application
- Weather data is fetched from OpenWeatherMap API using the `requests` library
- The frontend is built with HTML, CSS, and JavaScript, with dynamic updates using fetch API
- Environment variables are used to securely store the API key
- Auto-update functionality is implemented using JavaScript's `setInterval` function

## Error Handling
- API request errors are caught and displayed to the user
- Invalid city selections are handled gracefully
- Network errors during weather data fetching are caught and reported

## Implemented Protections
- API key is stored as an environment variable to prevent exposure
- Input validation is performed on the server-side to prevent injection attacks
- HTTPS is recommended for production deployment to encrypt data in transit
- CSRF protection is implemented using Flask-WTF to prevent cross-site request forgery attacks

## Advantages of this Implementation
- Separation of concerns between frontend and backend
- Easy to maintain and extend with modular code structure
- Responsive design works well on various device sizes
- Real-time data updates provide current weather information
- Minimal dependencies make the application lightweight and fast

## Future Improvements
- Add more cities or allow custom city input
- Implement caching to reduce API calls and improve performance
- Add historical weather data and forecasting
- Improve UI/UX with weather icons and animations
- Implement user accounts for saving favorite cities

## Contributing
Contributions to improve the Indian Weather Dashboard are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information.


## Acknowledgements
- [OpenWeatherMap](https://openweathermap.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Font Awesome](https://fontawesome.com)
