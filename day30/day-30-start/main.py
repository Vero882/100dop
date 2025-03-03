# File not found error
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# Try exceptions introducction
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["lkjasdf"])

# except FileNotFoundError: # This narrows down the except block to only catch FileNotFoundError
#     file = open("a_file.txt", "w")
#     file.write("Something")

# except KeyError as error_message: # This narrows down the except block to only catch KeyError and stores the error message in error_message to pass back to the user
#     print(f"The key {error_message} does not exist.")

# else: # This block will only run if no exceptions are raised in the try block
#     content = file.read()
#     print(content)

# finally: # This block will always run regardless of exceptions
#     # file.close()
#     # print("File was closed.")

# # Raising exceptions
#     raise TypeError("This is an error that I made up.") # This will create a TypeError at will. This is useful for debugging and testing.

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
