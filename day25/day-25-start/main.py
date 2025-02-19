#

# Utilizing just opening the file; difficult to parse data.
# data = []
# with open("day25/day-25-start/weather_data.csv") as data_file:
#     list_data = [data.strip("\n") for data in data_file.readlines()]
#     data.append(list_data)
# print(data)

# Utilizing csv.reader to parse data; easier to work with, but still needs a lot of lines to access a single column of data. 
# import csv
# with open("day25/day-25-start/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

    # for row in data:
    #     print(row)

# Utilizing pandas to parse data; much easier to work with.
import pandas

# These two lines perform the same function as above, to access a single column of data.
data = pandas.read_csv("day25/day-25-start/weather_data.csv")
# print(type(data)) # A full table is a DataFrame.
# print(type(data["temp"])) # A single column is a Series.

# data_dict = data.to_dict() # Converts the entire table to a nested dictionary with the column names as keys. 
# print(data_dict)

# temp_list = data["temp"].to_list() # Converts an entire column to a list.
# print(temp_list)

# # average_temp = sum(temp_list) / len(temp_list) # Calculates the average temperature.
# # print(f"Average temp: {average_temp}")

# print(f"Average temp: {data["temp"].mean()}") # Calculates the average temperature using a Panda built-in method.
# print(f"Max temp: {data["temp"].max()}") # Calculates the maximum temperature using a Panda built-in method.

# # Different ways of access data.
# print(data["condition"]) # Accesses a single column of data using bracket notation, similar to a dictionary.
# print(data.condition) # Accesses a single column of data using dot notation, similar to an object.

# Get data in rows.
# print(data[data.day == "Monday"]) # Print the entire row where the day is Monday.
# print(data[data.temp == data.temp.max()]) # Print the entire row with the maximum temperature.

# # This allows you to tap into a specific value within a row.
# monday = data[data.day == "Monday"] 
# print(monday.condition)

# # Convert Monday's temperature from Celsius to Fahrenheit.
# monday_temp = int(monday.temp)
# monday_temp_f = (monday_temp * 9/5) + 32
# print(monday_temp_f)

# Create a DataFrame from scratch.
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
report_card = pandas.DataFrame(data_dict)
report_card.to_csv("day25/day-25-start/report_card.csv") # Save the DataFrame to a CSV file.
