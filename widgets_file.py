import csv
import ipywidgets as widgets
from IPython.display import display

firstname = widgets.Text(description="Vorname:", value="")
display(firstname)

lastname = widgets.Text(description="Nachname:", value="")
display(lastname)

subject_options = [
    "---",
    "Mathe",
    "Informatik",
    "Philosophie",
    "Kulturwissenschaften",
    "Psychologie"
]

subject = widgets.Dropdown(description="Fach:", options=subject_options)
display(subject)

button = widgets.Button(description="Speichern!")
display(button)


def button_click(event):
    firstname_value = firstname.value
    lastname_value = lastname.value
    subject_value = subject.value

    if firstname_value != "" and lastname_value != "" and subject_value != "---":
        with open("./students.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow([firstname_value, lastname_value, subject_value])
        firstname.value = ""
        lastname.value = ""
        subject.value = "---"

    else:
        print("Bitte das Formular korrekt ausfüllen")


button.on_click(button_click)