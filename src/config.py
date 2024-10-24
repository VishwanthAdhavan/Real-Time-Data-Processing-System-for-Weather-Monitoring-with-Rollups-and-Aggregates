import os
from dotenv import load_dotenv
from pathlib import Path

# Get the base directory of your project
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
load_dotenv(BASE_DIR / '.env')

API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
CITIES = ['Mumbai', 'Delhi', 'Bangalore', 'Kolkata', 'Chennai']  # Add more cities as needed
