# Python Chapter 18 - Part 231
import pandas as pd
df = pd.read_csv("vocabulary.csv")
## output first 5 rows
print(df.head())
## length of list
print(len(df))
## column
## print(df["English"])
## row - index 0
print(df.iloc[0])