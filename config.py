import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
