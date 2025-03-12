# This script gets the weather for the next 12 hours and sends a text message if it will rain. 
# This utilizes the OpenWeatherApp API and the Twilio API and you will need accounts on both.

import requests
from twilio.rest import Client

# OpenWeatherApp API
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
WEATHER_API_KEY = "YOUR_WEATHER_API_KEY"
MY_LAT = YOUR_LATITUDE
MY_LON = YOUR_LONGITUDE


weather_params = {
    "appid": WEATHER_API_KEY,
    "lat": SAP_LAT,
    "lon": SAP_LON,
    "cnt": 4,
}

# Twilio API
SID = "YOUR_TWILIO_SID"
TWILIO_API_KEY = "YOUR_TWILIO_API_KEY"
TWILIO_NUMBER = "YOUR_TWILIO_NUMBER"
SEND_TO = "YOUR_PHONE_NUMBER"

account_sid = SID
auth_token = TWILIO_API_KEY
client = Client(account_sid, auth_token)

response = requests.get(API_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for i in range(4):
    if weather_data["list"][i]["weather"][0]["id"] < 700:
        will_rain = True
    
if will_rain:
    # print("Bring an umbrella.")
    message = client.messages.create(
        body="Bring an umbrella.",
        from_=TWILIO_NUMBER,
        to=SEND_TO,
    )
