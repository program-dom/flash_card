from tkinter import *
import pandas
from random import randint
BACKGROUND_COLOR = "#B1DDC6"
english_word = None
french_word = None
data = 0
#------------------------------READ DATA-----------------------------#

try:
    data = pandas.read_csv("data/words_to_learn.cvs")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    list_of_words = data.to_dict(orient="records")

#-----------------------------PROCESS DATA---------------------------#


def get_word():
    global english_word, timer, french_word
    window.after_cancel(timer)

    number = randint(0, 68)
    french_word = list_of_words[number]["French"]
    english_word = list_of_words[number]["English"]
    canvas.itemconfig(canvas_image, image=front)
    canvas.itemconfig(title, fill="black", text="French")
    canvas.itemconfig(word, fill="black", text=french_word)

    timer = window.after(4000, func=correct_word)


def after_click():
    list_of_words.remove({"French": french_word, "English": english_word})
    df = pandas.DataFrame(list_of_words)
    df.to_csv("data/words_to_learn.cvs", index=False)


def correct_word():
    canvas.itemconfig(canvas_image, image=back)
    canvas.itemconfig(title, fill="white", text="English")
    canvas.itemconfig(word, fill="white", text=english_word)

#------------------------------UI-------------------------------#


window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=correct_word)

# creating the canvas...
canvas = Canvas(height=532, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front)
title = canvas.create_text(400, 150, text="Text", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# creating the buttons...
right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=lambda: [get_word(), after_click()])
right_button.grid(column=0, row=1)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=get_word)
wrong_button.grid(column=1, row=1)

get_word()




window.mainloop()