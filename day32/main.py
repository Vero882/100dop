# Description: This program sends a birthday email to a person whose birthday is today.

import smtplib
import datetime as dt
import pandas as pd
import random

EMAIL = "MY_EMAIL"
PASSWORD ="MY_PASSWORD"
SMTP_SERVER = "smtp.gmail.com"
PORT = 587

today = dt.datetime.now()
today_month = today.month
today_day = today.day

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if (today_month, today_day) in birthdays_dict:
    birthday_person = birthdays_dict[(today_month, today_day)]
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP(SMTP_SERVER, PORT) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{letter}"
        )
    print(f"Email sent to {birthday_person["name"]}")

else:
    print("No birthdays today.")


