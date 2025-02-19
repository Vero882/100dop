# This script generates the new daily folder and the required README file for that day.

import os

# Set the day number
DAY_NUMBER = 25

# These lines do not need to be edited
FOLDER_NAME = f"day{DAY_NUMBER}"

# Create the folder
os.mkdir(FOLDER_NAME)

# Open the README template and write the new README file
with open("README.md.tmp") as template:
    readme = template.read()

    with open(f"./{FOLDER_NAME}/README.md", "w") as new_day:
        readme = readme.replace("[day]", str(DAY_NUMBER))
        new_day.write(readme)