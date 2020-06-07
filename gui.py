import tkinter

def leftClickButtonCheck():
    pass

my_vocable = "my vocable"

window = tkinter.Tk()

label_title = tkinter.Label(window, text="Vocabulary trainer")
label_title.pack()

button_check = tkinter.Button(window, text="Check")
button_check.pack()

label_vocable = tkinter.Label(window, text="Translate the following, please: " + my_vocable)
label_vocable.pack()

entry_solution = tkinter.Entry(window)
entry_solution.pack()

button_check.bind('<Button-1>', leftClickButtonCheck)

window.mainloop()