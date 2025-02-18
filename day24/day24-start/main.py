# Reading a file and printing its contents
# with open("./day24/day24-start/file.txt") as file:
#     contents = file.read()
#     print(contents)

# Writing to a file
# File is opened in read mode by default and we need to specify write mode (mode="w")
# If you don't want to wipe the file, you can use append mode (mode="a")
with open("file.txt", mode="a") as file: 
    file.write("\nThis is a second test line!")

# If file doesn't exist, it will be created
# The append mode will also create the file if it doesn't exist
with open("new_file.txt", mode="a") as file: 
    file.write("\nThis is a brand new file")