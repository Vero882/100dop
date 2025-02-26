from tkinter import *

def button_clicked():
    my_label.config(text=input.get())

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20) # Padding around the window.

# Label

my_label = Label(text="I am a label", font=("Arial", 24, "bold")) # Creating a label is not enough, you need to "pack" it into the window.

my_label["text"] = "New Label" # You can also change the text of the label using dictionary syntax.
my_label.config(text="New new Label", padx=50, pady=50) # Or using the config method. This allows updating multiple properties at once.

my_label.grid(column=0, row=0) # You can use the grid method to add the label to the window and change formatting. Pack can not be used with grid.
# my_label.place(x=100, y=0) # Place allows you to specifiy exact location of items, but you have to maintain the layout yourself.
# my_label.pack() # You can use the pack method to add the label to the window and change formatting.

# Button

button = Button(text="Click Me", command=button_clicked) # The command parameter allows you to specify a function to run when the button is clicked.
# button.pack()
button.grid(column=1, row=1)

# New Button
new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry

input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)


window.mainloop() # This will keep the window open and must be at the end of your code.