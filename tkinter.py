# import tkinter into global namespace
from tkinter import *
import tkinter as tk

# import ttk or themed tk library
from tkinter import ttk
from tkinter.ttk import *

# create root application object
root = tk.Tk()

# minimum size
root.minsize(600,400)

# title
root.title("Simple GUI")

# add label
label = Label(root, text="Hello all")
# before just
# label.pack()
# now we use grid
label.grid(column=1, row=0)

# add button
button = ttk.Button(root, text="Click me")
button.grid(column=0, row=0)

#add line to start our main event loop
root.mainloop()