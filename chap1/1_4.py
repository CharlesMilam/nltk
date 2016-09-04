import numpy
import matplotlib
from nltk.book import *

# get length of text3 - book of Genesis
print('Genesis has ' + str(len(text3)) + ' words.')

# find number of occurrences and percentage for 'lol'
lol_cnt = float(text5.count('lol'))
chat_len = float(len(text5))
print(lol_cnt)
print(100 * (lol_cnt / chat_len))

# create function to determine lexical diversity
def lex_div(text):
    return 100 * (float(len(set(text))) / float(len(text)))

#create function to determine %
def percentage(count, total):
    return 100 * (float(count) / float(total))

# print lexical diversity of Genesis
print(lex_div(text3))

# print %
count = text4.count('a')
total = len(text4)
print(percentage(count, total))
