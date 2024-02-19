from tkinter import *

root = Tk()
label1 = Label(root, text = "Enter digit:")
label1.grid(column = 0, row = 0)
entry = Entry(root, bd =5)
entry.grid(column = 0, row = 1)

FILE = 'Pi.txt'
TK_SILENCE_DEPRECATION=1
correct_guesses = 0
mistakes_left = 5

root.mainloop()

with open(FILE, 'r') as f:
    pi = f.read()

while True:
    guess = entry.get()
    print(guess)
    entry.delete(0, END)
    if guess != "":
        if guess == pi[correct_guesses]:
            print("Correct")
            correct_guesses += 1
        elif mistakes_left <= 0:
            break
        else:
            mistakes_left -= 1
            print("Incorrect")
    

print(f"You got {correct_guesses} digits correct")