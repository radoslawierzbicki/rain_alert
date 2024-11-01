import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Ładuje zmienne środowiskowe z pliku .env
api_key = os.getenv("API_KEY")

OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_params ={
    "appid": api_key,
    "q": "Gdańsk", "lat": 54.352024, "lon": 18.646639}

response = requests.get(OMW_Endpoint, params=weather_params)
print(response.json())