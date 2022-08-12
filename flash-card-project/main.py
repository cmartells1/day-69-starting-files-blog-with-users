import random
from tkinter import *
import pandas


BACKGROUND_COLOR = "#B1DDC6"

word_data = pandas.read_csv("data/french_words.csv")
word_list = word_data.to_dict(orient="records")
current_card= {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=flash_card_image_fr)
    current_card = random.choice(word_list)
    canvas.itemconfig(card_title, text='French', fill="black")
    canvas.itemconfig(card_word, text=current_card['French'],fill="black")
    flip_timer = window.after(3000, switch_card)

def switch_card():
    canvas.itemconfig(canvas_image, image=flash_card_image_eng)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer= window.after(3000, switch_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card_image_fr = PhotoImage(file="images/card_front.png")
flash_card_image_eng = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400,263, image=flash_card_image_fr)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, 'italic'))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

x_image = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0, command=next_card)
x_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=next_card)
check_button.grid(column=1, row=1)

next_card()

window.mainloop()
