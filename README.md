# Weather Notification Bot 🌦️

This Python project is a weather notification bot that checks the weather forecast and sends an SMS alert if rain is expected within the next few hours. The bot uses the OpenWeatherMap API to fetch weather data and the Twilio API to send SMS notifications. The program is designed to be run on a regular schedule using PythonAnywhere's task scheduler, ensuring timely notifications every day.

## Features

- **Fetches weather forecast** for a specified location (Gdańsk, Poland in this example).
- **Checks for rain** within the next few hours.
- **Sends an SMS alert** via Twilio if rain is detected, reminding you to bring an umbrella.

## Technologies Used

- **Python** - Primary programming language.
- **OpenWeatherMap API** - For accessing weather forecast data.
- **Twilio API** - For sending SMS notifications.
- **PythonAnywhere** - To schedule the script to run at regular intervals.

## Requirements

Install the necessary libraries by running:
```bash
pip install -r requirements.txt
```
## Environment Variables

To securely store your API keys and other sensitive information, create a `.env` file in the root directory of your project. Add the following variables to the file:

```plaintext
API_KEY=your_openweathermap_api_key
ACCOUNT_SID=your_twilio_account_sid
AUTH_TOKEN=your_twilio_auth_token
```
Replace your_openweathermap_api_key, your_twilio_account_sid, and your_twilio_auth_token with your actual keys.

Automating with PythonAnywhere

You can automate the script to run at regular intervals using PythonAnywhere, allowing you to receive notifications daily without manual execution.

    Sign up or log in to PythonAnywhere.
    Go to the Tasks tab in your PythonAnywhere dashboard.
    Schedule main.py to run at your desired time each day.

This will ensure the bot checks the weather and sends SMS alerts automatically.
