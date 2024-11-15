from tkinter import *
from tkmacosx import Button

# Window creation, root of the interface
window = Tk()

# Creation of a label (text line) that says Hello World ! and with as first parameter the previous window
label_field = Label(window,text="Hello World !")

# Display of the label
label_field.pack()

# Running of the Tkinter loop that ends when we close the windw
window.mainloop()

import tkinter as tk


def write_text():
    print("Hello CentraleSupelec")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   text="QUIT",
                   activebackground = "blue",
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   fg="blue",
                   text="Hello",
                   command=write_text)
slogan.pack(side=tk.UP)

root.mainloop()

