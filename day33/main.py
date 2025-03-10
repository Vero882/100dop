import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 39.74468131089976 # Your latitude
MY_LONG = -104.9707881535642 # Your longitude
YOUR_EMAIL = "email@gmail.com" # Your email
YOUR_PASSWORD = "password123" # Your app password

def iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
            return True
    else:
        return False

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    else:
        return False

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    if iss_close() and is_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(
                user=YOUR_EMAIL,
                password=YOUR_PASSWORD
            )
            connection.sendmail(
                from_addr=YOUR_EMAIL,
                to_addrs=YOUR_EMAIL,
                msg="Subject:Look Up\n\nThe ISS is above you in the sky."
            )

    time.sleep(60)



