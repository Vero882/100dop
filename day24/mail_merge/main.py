#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("day24/mail_merge/Input/Names/invited_names.txt") as file:
    namelist = [name.strip("\n") for name in file.readlines()]
print(namelist)

for name in namelist:
    with open("day24/mail_merge/Input/Letters/starting_letter.txt") as file:
        with open(f"day24/mail_merge/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter:
            letter.write(file.read().replace("[name]", name))