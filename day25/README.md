# Day 25 - Intermediate - Working with CSV data and the Pandas library
This day covers working with csv and other data files, and utilizing the data analysis library Pandas.  

## The video lessons are:
189. Day 25 goals: what we will make by the end of the day
190. Reading CSV data in Python
191. DataFrames & Series: Working with Rows and Columns
192. The Great Squirrel Census data analysis (with Panads!)
193. U.S. States game part 1: setup
194. U.S. States game part 2: challenge with .csv
195. U.S. States game part 3: Saving data to .csv

## Day 25 Project
The project for today is a U.S. state guessing game. The goal is to name all 50 states and have the names applied to a map. 

### Files provided:
- main.py
- blank_states_img.gif
- 50_states.csv

## Thoughts
This was an interesting project. referencing the information wasn't too difficult with the use of pandas, but I had some initial troubles with comparing the user answer to the dataset as it was throwing an ambiguous value error when trying to compare them. This was solved by utilizing the .any() function. Overall, I can see how this would be valuable in certain environments. 

I also ran into an issue through testing where the game would complete before I had guessed all of the states, and I realized it was because I was guessing the same state multiple times. So I started putting the user guesses into a list and making sure no repeat guesses were counted. 