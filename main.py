import pandas as pd
import random

df = pd.read_csv("vocabulary.csv")

# used random to get one set of a word in 3 languages
random_index = random.randint(1, len(df)-1)
vocabulary_set_entry = df.iloc[random_index]
vocabulary_set = vocabulary_set_entry[0].split(";")

class Vocabulary():

    def __init__(self, en, de, fr):
        self.en = en
        self.de = de
        self.fr = fr

    def show(self):
        print(self.en)
        print(self.de)
        print(self.fr)


voc = Vocabulary(vocabulary_set[0], vocabulary_set[1], vocabulary_set[2])
voc.show()