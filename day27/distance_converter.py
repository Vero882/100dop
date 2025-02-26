# This is a basic program that converts miles to kilometers to the second decimal place.

from tkinter import *

def convert():
    miles = float(input.get())
    km = round(miles * 1.609, 2)
    result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)

input = Entry(width=10)
input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1) 

calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)


window.mainloop()