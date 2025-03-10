import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json") # Contacts the API endpoint (URL) with the .get method
# # print(response) # Prints the response code (200 means success), not the actual data
# response.raise_for_status() # Raises an exception if the response code is not 200

# data = response.json() # Converts the JSON data into a Python dictionary. 
# longitude = data["iss_position"]["longitude"] # Can drill down into the dictionary to get the data you want.
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position) 

# Response code examples
# 1XX: Pending
# 2XX: OK
# 3XX: Auth Denied
# 4XX: You screwed up
# 5XX: I screwed up

MY_LAT = 39.74468131089976
MY_LNG = -104.9707881535642

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters) # Contacts the API endpoint (URL) with the .get method
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise.split("T")[1].split(":")[0])

time_now = datetime.now()
print(time_now.hour)