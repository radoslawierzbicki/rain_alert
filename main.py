import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()  # Ładuje zmienne środowiskowe z pliku .env
api_key = os.getenv("API_KEY")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_params ={
    "appid": api_key,
    "lat": 61.664837, "lon": 6.816487,
    "cnt": 4}

response = requests.get(OMW_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to take an umbrella!",
        from_='+phone_number',
        to='+phone_number'
    )
    print(message.status)