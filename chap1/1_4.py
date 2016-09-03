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
