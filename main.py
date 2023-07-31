
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
random_num = 0
french_word = ""
english_word = ""
word = ""

window = Tk()
window.title("Flash Cards")
window.config(bg = BACKGROUND_COLOR)

# ------------------------------- WORD BANK ----------------------------------- #

data = pandas.read_csv("c:/Users/personal/Python project/flash-card-project-start/data/french_words.csv")
data_dict = data.to_dict() 

# ----------------------------- NEW WORD DATABASE --------------------------------- #

def correct_words():
    global word

    try:
        with open("c:/Users/personal/Pyhton project/flash-card-project-start/data/words_to_learn.csv", "r") as file:
            content = file.read()
    except FileNotFoundError:
        new_dict = {row.French: row.English for (index, row) in data.iterrows() if data_dict['French'][random_num] != row.French}
        new_data = pandas.DataFrame(new_dict)
        new_data.to_csv("c:/Users/personal/Pyhton project/flash-card-project-start/data/words_to_learn.csv")
    else:
        word = pandas.read_csv("c:/Users/personal/Python project/flash-card-project-start/data/words_to_learn.csv")
        new_dict = {row.French: row.English for (index, row) in word.iterrows() if french_word != row.French}
        new_data = pandas.DataFrame(new_dict)
        new_data.to_csv("c:/Users/personal/Pyhton project/flash-card-project-start/data/words_to_learn.csv")

# ---------------------------- WORD GENERATION -------------------------------- #

def new_words():
    global data_dict
    global random_num
    global french_word
    global word

    correct_words()
    random_num = random.randint(0, len(data) - 1)
    try:
        with open("c:/Users/personal/Pyhton project/flash-card-project-start/data/words_to_learn.csv", "r") as file:
            content = file.read()
    except FileNotFoundError:
        french_word = data_dict['French'][random_num]
    else:
        for (index, row) in word.iterrows():
            if random_num == index:
                french_word = row.French
    canvas.itemconfig(word_text, text = french_word, fill = "Black")
    canvas.itemconfig(country_text, text= "French", fill = "Black")
    canvas.itemconfig(my_img, image = card_front)
    card_flip = window.after(3000, flip)

# ----------------------------- CARD FLIPPING  --------------------------------- #

def flip():
    global random_num
    global english_word
    
    try:
        with open("c:/Users/personal/Pyhton project/flash-card-project-start/data/words_to_learn.csv", "r") as file:
            content = file.read()
    except FileNotFoundError:
        english_word = data_dict['English'][random_num]
    else:
        for (index, row) in word.iterrows():
            if random_num == index:
                english_word = row.English
    canvas.itemconfig(my_img, image = card_back)
    canvas.itemconfig(country_text, text= "English", fill = "white")
    canvas.itemconfig(word_text, text = english_word, fill = "white")

# -------------------------------- UI SETUP ----------------------------------- #

card_front = PhotoImage(file = "c:/Users/personal/Python project/flash-card-project-start/images/card_front.png")
card_back = PhotoImage(file = "c:/Users/personal/Python project/flash-card-project-start/images/card_back.png")

canvas = Canvas(width= 800, height= 526)
my_img = canvas.create_image(400, 263, image = card_front)
canvas.config(bg = BACKGROUND_COLOR, highlightthickness= 0)
canvas.grid(row=0, column=0, columnspan= 2, padx= 50, pady= 50)


country_text = canvas.create_text(400, 150, text="Language", font= ("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font= ("Ariel", 60, "bold"))

right_image = PhotoImage(file = "c:/Users/personal/Python project/flash-card-project-start/images/right.png")
right_button = Button(image = right_image, highlightthickness = 0, padx= 50, command = new_words)
right_button.grid(row = 1, column=0)

wrong_image = PhotoImage(file = "c:/Users/personal/Python project/flash-card-project-start/images/wrong.png")
wrong_button = Button(image = wrong_image, highlightthickness = 0, padx= 50, command = new_words)
wrong_button.grid(row= 1, column=1)

window.mainloop()

# ---------------------------------------------------------------------------- #
