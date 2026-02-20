from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
curr_card = {}
learn_d = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    og_data = pd.read_csv("data/french_words.csv")
    learn_d = og_data.to_dict(orient="records")
else:
    learn_d = data.to_dict(orient="records")

def next_card():
    global curr_card, flip_timer
    window.after_cancel(flip_timer)
    curr_card = random.choice(learn_d)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=curr_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=curr_card["English"], fill="black")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    learn_d.remove(curr_card)
    data = pd.DataFrame(learn_d)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
    
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images\card_front.png")
card_back_img = PhotoImage(file="images\card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="language", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

wrong_img = PhotoImage(file="images\wrong.png")
uk_button = Button(
    image=wrong_img,
    highlightthickness=0,
    bd=0,
    bg=BACKGROUND_COLOR,
    activebackground=BACKGROUND_COLOR,
    command=next_card,
)
uk_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
k_button = Button(
    image=right_img,
    highlightthickness=0,
    bd=0,
    bg=BACKGROUND_COLOR,
    activebackground=BACKGROUND_COLOR,
    command=is_known,
)
k_button.grid(row=1, column=1)

next_card()

window.mainloop()