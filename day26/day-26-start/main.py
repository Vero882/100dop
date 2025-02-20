# This is an example of using list comprehension in Python
numbers = [1, 2, 3]
# Format should be [new_item for item in list
new_list = [n + 1 for n in numbers] 

# Not restricted to just numbers
name = "Link"
letters_list = [letter for letter in name]

doubled_range = [item * 2 for item in range(1,5)]

# Conditional list comprehension
# Format should be [new_item for item in list if test]
names = ["Zelda", "Link", "Ganondorf"]
short_names = [name for name in names if len(name) < 5] 
long_names = [name.upper() for name in names if len(name) >= 5]


# Dictionary comprehension
# Format should be {new_key:new_value for item in list}
# Or {new_key:new_value for (key, value) in dict.items()}
# Conditionals can be added to the end as well
import random
names = ["Zelda", "Link", "Ganondorf"]
student_scores = {name: random.randint(1, 100) for name in names}
passed_students = {name:score for (name, score) in student_scores.items() if score >= 60}


# Iterate over a Panda DataFrame
import pandas

student_dict = {
    "student": ["Link", "Zelda", "Ganondorf"],
    "score": [75, 90, 80]
}
student_dataframe = pandas.DataFrame(student_dict)
# print(student_dataframe)

# Pandas built-in loop is iterrows()
for (index, row) in student_dataframe.iterrows():
    # print(index) # Returns the index
    # print(row) # Returns each row
    # print(row.student) # Returns the student name
    if row.student == "Link":
        print(row.score)
