import requests
import smtplib
from newsapi import NewsApiClient
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "YOUR_STOCK_API_KEY"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"

YOUR_EMAIL = "email@gmail.com" # Your email
YOUR_PASSWORD = "YOUR_EMAIL_PASSWORD" # Your app password

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])
difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
percentage = (difference / yesterday_closing_price) * 100

if percentage > 5:
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    three_articles = news_data[:3]
    three_articles_data = [f"Headline: {article["title"]}. \nBrief: {article["description"]}\n\n" for article in three_articles]

    SID = "YOUR_TWILIO_SID"
    TWILIO_API_KEY = "YOUR_TWILIO_API_KEY"
    TWILIO_NUMBER = "YOUR_TWILIO_NUMBER"
    SEND_TO = "YOUR_PHONE_NUMBER"

    account_sid = SID
    auth_token = TWILIO_API_KEY
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"{STOCK} Movement\n\n{STOCK} {'-' if percentage > 0 else '+'} {round(percentage, 2)}%",
        from_=TWILIO_NUMBER,
        to=SEND_TO,
    )

else:
    print("No News")


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.


# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(
#         user=YOUR_EMAIL,
#         password=YOUR_PASSWORD
#     )
#     connection.sendmail(
#         from_addr=YOUR_EMAIL,
#         to_addrs=YOUR_EMAIL,
#         msg=f"Subject:{STOCK} Movement\n\n{STOCK} {'-' if percentage > 0 else '+'} {round(percentage, 2)}%\n\n"
#     )
# print(f"Subject:{STOCK} Movement\n\n{STOCK} {'-' if percentage > 0 else '+'} {round(percentage, 2)}%\n\n{a1}\n{a2}\n{a3}")