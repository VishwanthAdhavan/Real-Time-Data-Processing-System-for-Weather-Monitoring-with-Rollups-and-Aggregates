import os
from dotenv import load_dotenv
from pathlib import Path

# Get the base directory of your project
BASE_DIR = Path(__file__).resolve().parent.parent

# Print the base directory and .env file path
print(f"Base directory: {BASE_DIR}")
print(f".env file path: {BASE_DIR / '.env'}")

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')

if not API_KEY:
    raise ValueError("No API key set for OpenWeatherMap. Please set OPENWEATHERMAP_API_KEY environment variable.")

# Print all environment variables (be careful with sensitive information)
print("All environment variables:")
for key, value in os.environ.items():
    if key == "OPENWEATHERMAP_API_KEY":
        print(f"{key}: {'*' * len(value)}")  # Mask the API key
    else:
        print(f"{key}: {value}")

CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']  # Add or modify cities as needed
UPDATE_INTERVAL = 300  # 5 minutes in seconds
TEMPERATURE_UNIT = "celsius"  # or "fahrenheit"

# Alerting thresholds
MAX_TEMPERATURE_THRESHOLD = 35
CONSECUTIVE_UPDATES_THRESHOLD = 2

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///weather_data.db")
