#----------------------SMTP Module Introduction----------------------#
# import smtplib

# # Create a connection to the SMTP server
# email = "email@gmail.com"
# password = "" # This should be the app password generated within security settings
# with smtplib.SMTP("smtp.gmail.com") as connection: # With statement will close the connection automatically

#     # Start the connection
#     connection.starttls()

#     # Authenticate the connection
#     connection.login(user=email, password=password)

#     # Send an email
#     connection.sendmail(
#         from_addr=email, 
#         to_addrs="send@mail.com", 
#         msg="Subject:Hello\n\nThis is the body of the email"
#     )

# # Close the connection similar to file.close()
# # connection.close()

#----------------------Datetime Module Introduction----------------------#
# import datetime as dt

# now = dt.datetime.now() # Get the current date and time
# year = now.year # Taps into the attribute of the datetime object to get the year
# month = now.month
# day_of_week = now.weekday() # Monday is 0 and Sunday is 6
# print(day_of_week)

# date_of_birth = dt.datetime(year=1999, month=1, day=1, hour=12) # You can specify custom date and time
# print(date_of_birth)


#----------------------Monday Motivational Quote Challenge----------------------#
import smtplib
import datetime as dt
import random

# Email credentials
EMAIL = "email@gmail.com"
PASSWORD = ""

# Get the current date and time
now = dt.datetime.now()
day_of_week = now.weekday()

# Get the motivational quotes
with open("quotes.txt") as file:
    quotes = file.readlines()

# Get the quote of the day
quote_of_the_day = random.choice(quotes)

# Send the email
if day_of_week == 0:
    print("Sending email...")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="recipient@email.com",
            msg=f"Subject:Happy Monday!\n\n{quote_of_the_day}"
        )
    print("Email sent successfully!")
else:
    print("Not Monday, no email sent.")
