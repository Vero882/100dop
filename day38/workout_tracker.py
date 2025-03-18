import requests
from datetime import datetime
import os
from dotenv import load_dotenv


load_dotenv()

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_headers = {
    "x-app-id": os.environ.get("NUTRI_APP_ID"),
    "x-app-key": os.environ.get("NUTRI_API_KEY"),
}

exercise_params = {
    "query": input("Tell me which exercises you did: "),
    "age": 35,
    "weight_kg": 85,
    "height_cm": 182,
}

response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=exercise_headers)
response.raise_for_status()
# print(response.json())

SHEETY_API = os.environ.get("SHEETY_API") 

sheety_headers = {
    "Authorization": os.environ.get("SHEETY_AUTH")
}

print("Adding exercises to Sheety...")
for exercise in response.json()["exercises"]:
    sheety_params = {
        "workout": {
            "date": datetime.now().strftime("%d %b %Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": str(exercise["duration_min"]),
            "calories": exercise["nf_calories"],
        }
    }
    
    sheety_response = requests.post(url=SHEETY_API, json=sheety_params, headers=sheety_headers)
    sheety_response.raise_for_status()

if sheety_response.status_code == 200:
    print("Exercises added successfully.")
    