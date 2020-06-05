# Python Chapter 18 - Part 231
import pandas as pd
df = pd.read_csv("vocabulary.csv")
df
## output first 5 rows
df.head()
## length of list
len(df)
## column
df["English"]
## row - index 0
df.iloc[0]
