# This is a simple habit tracker app.

import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "YOUR USERNAME"
TOKEN = "YOUR_TOKEN" # This is essentially your password and is a custom token that you create.

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params) # Create a new user
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "NAME OF YOUR GRAPH",
    "unit": "hours",
    "type": "int",
    "color": "shibafu",
    # "timezone": "", # This is an optional field for the users timezone
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers) # Create a new graph based on the above config
# print(response.text)

# update_graph = requests.put(url=f"{GRAPH_ENDPOINT}/graph1", json={"color": "momiji"}, headers=headers) # Update an existing graph
# print(update_graph.text)

PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1"

today = datetime.now() # To supply a specific date use datetime(year= , month= , day= )

pixel_config = {
    "date": today.strftime("%Y%m%d"), # Format the date as YYYYMMDD
    "quantity": "1", # The amount of time spent on the habit; this could also be an input from the user. 
}

# Create a new pixel based on the above config
# response = requests.post(url=PIXEL_ENDPOINT, json=pixel_config, headers=headers) 
# print(response.text)

# Update an existing pixel
# update = requests.put(url=f"{PIXEL_ENDPOINT}/{today.strftime('%Y%m%d')}", json={"quantity": "2"}, headers=headers)
# print(update.text)

# Delete an existing pixel
# delete = requests.delete(url=f"{PIXEL_ENDPOINT}/{today.strftime('%Y%m%d')}", headers=headers)
# print(delete.text)