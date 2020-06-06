import pandas as pd
import random

# read in vocabulary sets
df = pd.read_csv("vocabulary.csv")

# used random to get one set of a word in 3 languages
random_index = random.randint(1, len(df)-1)
vocabulary_set_entry = df.iloc[random_index]
vocabulary_set = vocabulary_set_entry[0].split(";")

# work with the vocabulary set
class Vocabulary():

    # define constructor
    def __init__(self, en, de, fr):
        self.en = en
        self.de = de
        self.fr = fr

    # show all selected words in all languages
    def show(self):
        print(self.en)
        print(self.de)
        print(self.fr)

# create vocabulary set, to further work with it as an object
voc = Vocabulary(vocabulary_set[0], vocabulary_set[1], vocabulary_set[2])

# show all words of the vocabulary set
voc.show()