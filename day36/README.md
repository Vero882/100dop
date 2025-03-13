# Day 36 - Intermediate+ Stock trading news alert project
This day covers creating our own Bloomberg Terminal to track stock trading and stock news. 

## The video lessons are:
275. Day 36 goals: what you will make by the end of the day
276. Choose your destiny!
277. Solution & walkthrough for step 1 - check for stock price movements
278. Solution & walkthrough for step 2 - Get the news articles
279. Solution & walkthrough for step 3 - Send the SMS messages

## Day 36 Project
The project for today is a Bloomberg Terminal to track stocks and their relevent news, and send an SMS message with important updates. 

### Files provided:
- main.py

## Thoughts
Today I've decided to go with the hard version of the starter project. Due to the issues outlined yesterday with Twilio I will use EMail for the notifications instead of SMS. Overall I had a handful of issues. Attempting to send it as an email resulted in some ascii errors from reading the article text and it trying to import encoded characters. Then when I went back to Twilio to just test that it was working the articles was going over the character limit for the text, so I had to shorten it down to just the movement percentage of the stock. 