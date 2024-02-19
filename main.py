from tkinter import *

FILE = 'Pi.txt'
correct_guesses = 0
mistakes_left = 5

with open(FILE, 'r') as f:
    pi = f.read()

def reset():
    global correct_guesses
    global mistakes_left
    correct_guesses = 0
    mistakes_left = 5
    update_mistakes()
    text.config(state = NORMAL)
    text.delete('1.0', END)
    text.insert(END, "3.")
    text.config(state = DISABLED)

def update_mistakes():
    global mistakes_left
    content_label_2.set(f"Mistakes left: {mistakes_left}")

def on_text_change(var):
    global mistakes_left
    global correct_guesses
    guess = var.get()
    entry.delete(0, END)
    if mistakes_left >= 0:
        if guess != "":
            if guess == pi[correct_guesses]:
                text.config(state = NORMAL)
                text.insert(END, guess)
                text.config(state = DISABLED)
                correct_guesses += 1
            elif mistakes_left == 0:
                mistakes_left -= 1
                content_label_2.set(f"You got {correct_guesses} digits correct")
                text.config(state = NORMAL)
                text.insert(END, pi[correct_guesses:20])
                text.config(state = DISABLED)
            else:
                mistakes_left -= 1
                update_mistakes()
TK_SILENCE_DEPRECATION = 1
root = Tk()
label1 = Label(root, text = "Enter digit:")
label1.grid(column = 0, row = 0)

text_var = StringVar()
text_var.trace_add('write', lambda *args: on_text_change(text_var))
entry = Entry(root, textvariable = text_var, bd = 5)
entry.grid(column = 0, row = 1)

content_label_2 = StringVar()
update_mistakes()
label2 = Label(root, textvariable = content_label_2)
label2.grid(column = 1, row = 1)

text = Text(root, width = 40, height = 20, font = ("Arial",20))
text.insert(END, "3.")
text.config(state = DISABLED)
text.grid(column = 0, row = 2)

restart_button = Button(root, text  = "restart", command = reset).grid(column = 0, row = 3)

exit_button = Button(root, text = "Quit", command=root.destroy).grid(column = 0, row = 4)
root.mainloop()