import numpy
import matplotlib
from nltk.book import *

# line break
lb = '+++++++++++++++++++++++++++++++++++++++++++++++++++++'

# get frequency distribution of Monty Python
fdist1 = FreqDist(text6)
print(fdist1)
print(lb)

# get the 50 most common tokens
print(fdist1.most_common(50))
print(lb)

# get the hapaxes
print(fdist1.hapaxes())
print(lb)

# plot fdist1
# fdist1.plot(50, cumulative = True)

# get long words
uniqs = set(text6)
long_words = [word for word in uniqs if len(word) > 10]
print(sorted(long_words))
print(lb)

# get collocations
print(text6.collocations())
