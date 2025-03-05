from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT = "./images/card_front.png"
CARD_BACK = "./images/card_back.png"
CROSS = "./images/wrong.png"
CHECK = "./images/right.png"

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("./data/french_words.csv")
    

to_learn = data.to_dict(orient="records")
current_card = random.choice(to_learn)

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language_label, text="French", fill="black")
    canvas.itemconfig(word_label, text=current_card["French"], fill="black")
    canvas.itemconfig(front, image=card_front)
    window.after(3000, flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=current_card["English"], fill="white")
    canvas.itemconfig(front, image=card_back)


window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file=CARD_FRONT)
card_back = PhotoImage(file=CARD_BACK)
check = PhotoImage(file=CHECK)
cross = PhotoImage(file=CROSS)

canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
front = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

language_label = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word_label = canvas.create_text(400, 300, text=current_card["French"], font=("Arial", 60, "bold"), fill="black")

button_wrong = Button(image=cross, highlightthickness=0, command=next_card)
button_wrong.grid(row=1, column=0)
button_right = Button(image=check, highlightthickness=0, command=is_known)
button_right.grid(row=1, column=1)

flip_timer = window.after(3000, flip_card)



window.mainloop()