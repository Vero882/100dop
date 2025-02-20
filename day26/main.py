# This project converts a user inputted word into a list of NATO phonetic alphabet words

import pandas


data = pandas.read_csv("day26/nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

user_input = input("Enter a word: ").upper()


nato_list = [nato_dict[letter] for letter in user_input]
print(nato_list)

