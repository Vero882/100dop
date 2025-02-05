# In order to utilize the PrettyTable module, I had to install it via pip, but I had to create a virtual environment first.
# I created a virtual environment by running the following command: 'python3 -m venv venv' and 'source venv/bin/activate' to enable.
# I then installed the prettytable module with 'pip install prettytable'.

from prettytable import PrettyTable

# Pause Challenge 3 (Lesson 112: 0:50) Create a PrettyTable obejct and save it to a variable called table.
table = PrettyTable()

# Pause Challenge 4 (Lesson 112: 2:43) Add columns to the table.
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# Pause Challenge 5 (Lesson 112: 6:24) Align the table to the left.
table.align = "l"

print(table)