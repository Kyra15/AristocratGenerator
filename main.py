# 500k quotes comes in a csv file
# Each row is a quoteand columns of the quote, author, and tags

# read the csv and ONLY get the first column (the quote)
# then assign each letter a random letter out of a list of the alphabet (use pop)
# replace the letters with the randomly assigned letter
# print the quote and start a timer while awaiting the user's input
# if the user's input is right or within 2 letters of the correct answer,
# print "correct" and print the time it took

import pandas as pd
import random
import functions as fn
import string

n = sum(1 for line in open("500kquotes.csv"))-1
s = n//20
skip = sorted(random.sample(range(1, n+1), n-s))

df = pd.read_csv('500kquotes.csv', usecols=["quote", "author"], skiprows=skip)

df['quote'] = df['quote'].astype('str')
df["author"] = df["author"].astype("str")
mask = (df["quote"].str.len() <= 150) & (df["author"].str.len() <= 100)
df = df.loc[mask]
df = df[~df["quote"].str.contains(r'\d')]

print(len(df))

str_index = random.randint(0, len(df) - 1)
print(str_index)

og_str = df.iloc[str_index, 0]
author = df.iloc[str_index, 1]
print("og", og_str)
print(f"Decode this quote from {string.capwords(author.strip().replace('.', ''))}:")

encoded = og_str.lower()

clean = [x for x in encoded if x.isalnum()]

uniq = {*clean}

encoded, freq = fn.assign(uniq, encoded)

if "\"" in encoded:
    encoded = "\"" + encoded + "\""
print("encoded:", encoded.upper())

fn.take_input(og_str, freq)


