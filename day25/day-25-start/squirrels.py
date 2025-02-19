# This script will pull data from a CSV file and figure out how many squirrels of each color were in the data set, and export it to it's own CSV.

import pandas

data = pandas.read_csv("day25/day-25-start/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

squirrels = {
    "Fur Color": ["grey", "cinnamon", "black"],
    "Count": [grey_squirrels, cinnamon_squirrels, black_squirrels]
}

total_squirrels = pandas.DataFrame(squirrels)
total_squirrels.to_csv("day25/day-25-start/squirrel_count.csv")