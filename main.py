"""
import csv

with open("vocabulary.csv", newline='', encoding="utf-8") as file:
    csv_file = csv.reader(file, delimiter=",")
    for line in csv_file:
        print(line)
"""

import pandas as pd
df = pd.read_csv("vocabulary.csv")

class Vocabulary():

    def __init__(self, en, de, fr):
        self.en = en
        self.de = de
        self.fr = fr

    def show(self):
        print(self.en)
        print(self.de)
        print(self.fr)

voc = Vocabulary("I","ich","moi")
voc.show()
