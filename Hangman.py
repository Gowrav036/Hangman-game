import random
from tkinter import *
from tkinter import messagebox

with open("words.txt", "r") as f:
    words = [word.strip() for word in f.readlines()]

score = 0

def start_game():
    global selected_word, guessed_letters, wrong_count
    
    selected_word = random.choice(words)
    guessed_letters = []
    wrong_count = 0
    
    word_label.config(text="_ " * len(selected_word))
    status_label.config(text="")
    
    for btn in buttons.values():
        btn.config(state=NORMAL)

def check_letter(letter):
    global wrong_count, score
    
    buttons[letter].config(state=DISABLED)
    
    if letter in selected_word:
        guessed_letters.append(letter)
        display_word = ""
        for char in selected_word:
            if char in guessed_letters:
                display_word += char + " "
            else:
                display_word += "_ "
        word_label.config(text=display_word)
        
        if "_" not in display_word:
            score += 1
            if messagebox.askyesno("GAME OVER", "You Won!\nPlay Again?"):
                start_game()
            else:
                root.quit()
    else:
        wrong_count += 1
        status_label.config(text=f"Wrong Attempts: {wrong_count}/6")
        
        if wrong_count == 6:
            if messagebox.askyesno("GAME OVER", f"You Lost!\nWord was: {selected_word}\nPlay Again?"):
                start_game()
            else:
                root.quit()

root = Tk()
root.title("HANGMAN")
root.geometry("600x500")
root.config(bg="#E7FFFF")

title = Label(root, text="HANGMAN GAME", font=("Arial", 24), bg="#E7FFFF")
title.pack(pady=10)

word_label = Label(root, text="", font=("Arial", 30), bg="#E7FFFF")
word_label.pack(pady=20)

status_label = Label(root, text="", font=("Arial", 14), bg="#E7FFFF")
status_label.pack()

buttons_frame = Frame(root, bg="#E7FFFF")
buttons_frame.pack(pady=20)

buttons = {}

alphabet = "abcdefghijklmnopqrstuvwxyz"

row = 0
col = 0

for letter in alphabet:
    btn = Button(buttons_frame, text=letter.upper(), width=4, height=2,
                 command=lambda l=letter: check_letter(l))
    btn.grid(row=row, column=col, padx=5, pady=5)
    buttons[letter] = btn
    
    col += 1
    if col == 9:
        col = 0
        row += 1

start_game()

root.mainloop()