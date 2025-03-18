# Day 38 - Intermediate+ Workout tracking using Google Sheets
This day is a challenge to create an exercise tracking application using Python and Google Sheets.

## The video lessons are:
286. Day 38 goals: what you will make by the end of the day
287. Step 1: Set up API credentials and Google spreadsheet
288. Step 2: Get exercise stats with Natural language quereries
289. Step 3: Set up your Google sheet with Sheetly
290. Step 4: Saving data into Google Sheets
291. Step 5: Authenticate your Sheety API
292. Step 6: Environment variables

## Day 38 Project
The project for today is to build a natural language powered exercise tracking application where you can type a natural sentance for the exercises you performed that day and it will be input automatically in Google Sheets columns. 

## Thoughts
I like that you can so easily interface with something as big as Google Sheets. I had a couple of issues with the duration populating as "01 min" continuously, so eventually I had to convert it to a string instead. I decided to go the extra bit and figure out how to use a .env file instead of having to continuously export variables every time I rebooted the computer, and that lead me to the dotenv library. 