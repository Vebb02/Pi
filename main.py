from tkinter import *

FILE = 'Pi.txt'
correct_guesses = 0
mistakes_left = 5

with open(FILE, 'r') as f:
    pi = f.read()

def clear_text():
    text.config(state = NORMAL)
    text.delete('1.0', END)
    text.insert(END, "3.")
    text.config(state = DISABLED)

def reset():
    global correct_guesses
    global mistakes_left
    correct_guesses = 0
    mistakes_left = 5
    update_mistakes()
    content_label_3.set("")
    clear_text()

def update_mistakes():
    global mistakes_left
    content_label_2.set(f"Mistakes left: {mistakes_left}")

def add_text(s: str):
    text.config(state = NORMAL)
    text.insert(END, s)
    text.config(state = DISABLED)

def on_text_change(var):
    global mistakes_left
    global correct_guesses
    guess = var.get()
    entry.delete(0, END)
    if mistakes_left >= 0:
        if guess != "":
            if guess == pi[correct_guesses]:
                add_text(guess)
                correct_guesses += 1
            elif mistakes_left == 0:
                mistakes_left -= 1
                content_label_2.set(f"You got {correct_guesses} digits correct")
                content_label_3.set(f"The next 20 digits are {pi[correct_guesses:correct_guesses + 20]}")
            else:
                mistakes_left -= 1
                update_mistakes()

root = Tk()
root.title("Pi Quiz")

label1 = Label(root, text = "Enter digit:")
label1.grid(column = 0, row = 0)

text_var = StringVar()
text_var.trace_add('write', lambda *args: on_text_change(text_var))
entry = Entry(root, textvariable = text_var, bd = 5)
entry.grid(column = 0, row = 1)

content_label_2 = StringVar()
update_mistakes()
label2 = Label(root, textvariable = content_label_2, font = ("Arial", 20))
label2.grid(column = 1, row = 1)

content_label_3 = StringVar()
label3 = Label(root, textvariable = content_label_3, font = ("Arial", 20))
label3.grid(column = 1, row = 2)

text = Text(root, width = 40, height = 20, font = ("Arial", 20))
text.insert(END, "3.")
text.config(state = DISABLED)
text.grid(column = 1, row = 3)

restart_button = Button(root, text  = "restart", command = reset).grid(column = 1, row = 4)

exit_button = Button(root, text = "Quit", command=root.destroy).grid(column = 1, row = 5)

root.mainloop()