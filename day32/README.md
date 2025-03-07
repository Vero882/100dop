# Day 32 - Intermediate+ Send email (smtplib) & Manage Dates (datetime)
This day covers sending emails utilizing SMTP, and managing automation of when to send those emails with the date manager module. 

## The video lessons are:
243. Day 32 goals: what we will make by the end of the day
244. A note about the next lessong: Google SMTP port
245. How to send emails with Python using SMTP
246. Working with the datetime module
247. Challenge 1 - Send motivation quotes on Mondays via email
248. Automated Birthday wisher project challenge
249. Solution & walkthrough for the automated birthday wisher
250. Run your Python code in the cloud

## Day 32 Project
The project for today is an automated happy birthday email to send out birthday cards autommatically.

### Files provided
- main.py 
- letter_templates
    - letter_1.txt
    - letter_2.txt
    - letter_3.txt
-birthdays.csv

## Thoughts
It's been an exhausting week, so I decided to pick the "normal" option for the project with the most hints, however I don't know that I really needed it. I had an issue initially with it sending the index number instead of the name because of the way Pandas worked, so I had to change from using attribute access to using dictionary access. Then everything worked just fine. I also added a couple of print statements to make it feel more user friendly for the person running the script so they know if a birthday message was sent out or not. 