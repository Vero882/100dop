from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    '''Generates a random password with 8-10 letters, 2-4 symbols, and 2-4 numbers.'''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    '''Saves the website, email, and password to a text file in the same directory.'''

    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0 or len(email_entry.get()) == 0:
        messagebox.showerror(title="Error", message="All fields are required!")
        return

    confirmation = messagebox.askyesno(title="Are you sure?", message=f"Details entered:\nWebsite: {website_entry.get()}\nEmail: {email_entry.get()}\nPassword: {password_entry.get()}\n\nIs this correct?")
    if not confirmation:
        return
    
    with open("data.txt", "a") as file:
        file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)
    website_entry.focus()
    messagebox.showinfo(title="Success", message="Password saved successfully!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(0, "user@defaultmail.com") # Default email value

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons

gen_pass_button = Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)





window.mainloop()