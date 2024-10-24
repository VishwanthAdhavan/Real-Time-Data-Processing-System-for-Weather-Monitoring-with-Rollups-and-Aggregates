import requests
import logging
from src.config import API_KEY
from urllib.parse import urlencode
import time

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def get_weather_data(city):
    start_time = time.time()
    logger.debug(f"[{start_time}] Fetching weather data for city: {city}")
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    
    full_url = f"{base_url}?{urlencode(params)}"
    logger.debug(f"Requesting URL: {full_url.replace(API_KEY, 'API_KEY')}")  # Log URL without exposing API key
    
    try:
        api_start_time = time.time()
        response = requests.get(base_url, params=params, timeout=10)  # 10 second timeout
        api_end_time = time.time()
        api_duration = api_end_time - api_start_time
        logger.debug(f"[{api_end_time}] API request took {api_duration:.2f} seconds")
        logger.debug(f"Response status code: {response.status_code}")
        
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        data = response.json()
        
        end_time = time.time()
        total_duration = end_time - start_time
        logger.debug(f"[{end_time}] Total weather data retrieval took {total_duration:.2f} seconds")
        
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "weather_condition": data["weather"][0]["main"],
            "description": data["weather"][0]["description"]
        }
    except requests.exceptions.RequestException as e:
        logger.error(f"Error making request to OpenWeatherMap API: {str(e)}")
        raise Exception(f"Error fetching weather data: {str(e)}")
    except KeyError as e:
        logger.error(f"Error parsing API response: {str(e)}")
        raise Exception(f"Error parsing weather data: {str(e)}")

logger.debug(f"get_weather_data function: {get_weather_data}")
