import tkinter as tk
from tkinter import messagebox
import random
import json

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ('Time Courier', 32, 'italic')
FONT_WORD = ('Time Courier', 64, 'bold')
FOREIGN_LANGUAGE = 'Japanese'
NATIVE_LANGUAGE = 'English'
flashcard_info = {}
# --------------------------- 💡💻 RUN PROGRAM 💻💡 ----------------------------
window = tk.Tk()
window.title('Flashcards')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)


# ----------------------------- 💡💻 GET DATA 💻💡 -----------------------------
def new_flashcard(data):
    return random.choice(list(data.items()))


try:
    with open('./data/words.json') as file:
        try:
            words = json.load(file)
        except:
            messagebox.showerror(title='File empty',
                                 message=('File is corrupted or empty\n'
                                          'Program will shut down')
                                 )
except FileNotFoundError:
    messagebox.showerror(title='File Not Found',
                         message='File is missing\nProgram will shut down.')
    window.destroy()


# -------------------- 💡💻 CHANGE FLASHCARD MECHANISM 💻💡 --------------------
def change_flashcard(which_button):
    global flashcard_info, flip_timer
    window.after_cancel(flip_timer)
    # Delete known word from file
    if which_button:
        del words[(flashcard_info[0])]
        with open('./data/words.json', mode='w') as file:
            json.dump(words, file, indent=4)

    flashcard_info = new_flashcard(words)
    foreign_word = flashcard_info[1][FOREIGN_LANGUAGE]
    card_canvas.itemconfig(language_canvas, text=f'{FOREIGN_LANGUAGE}',
                           fill='black')
    card_canvas.itemconfig(word_canvas, text=f'{foreign_word}', fill='black')
    card_canvas.itemconfig(background_canvas, image=card_front)
    flip_timer = window.after(3000, flip_flashcard)


def flip_flashcard():
    native_word = flashcard_info[1][NATIVE_LANGUAGE]
    card_canvas.itemconfig(language_canvas, text=f'{NATIVE_LANGUAGE}',
                           fill='white')
    card_canvas.itemconfig(word_canvas, text=f'{native_word}', fill='white')
    card_canvas.itemconfig(background_canvas, image=card_back)


# ----------------------------- 💡💻 SETUP UI 💻💡 -----------------------------
card_front = tk.PhotoImage(file='./images/card_front.png')
card_back = tk.PhotoImage(file='./images/card_back.png')
right_img = tk.PhotoImage(file='./images/right.png')
wrong_img = tk.PhotoImage(file='./images/wrong.png')

card_canvas = tk.Canvas(width=800, height=525, bg=BACKGROUND_COLOR,
                        highlightthickness=0)
background_canvas = card_canvas.create_image(410, 270, image=card_front)
language_canvas = card_canvas.create_text(410, 150, text='Language',
                                          font=FONT_LANGUAGE)
word_canvas = card_canvas.create_text(410, 300, text='Word', font=FONT_WORD)
card_canvas.grid(row=0, column=0, columnspan=2)

wrong_button = tk.Button(image=wrong_img, highlightthickness=0, bd=0,
                         command=lambda: change_flashcard(False))
wrong_button.grid(row=1, column=0)

right_button = tk.Button(image=right_img, highlightthickness=0, bd=0,
                         command=lambda: change_flashcard(True))
right_button.grid(row=1, column=1)
flip_timer = window.after(3000, flip_flashcard)
change_flashcard(False)

window.mainloop()
