from nltk.book import *

# helper line breaks
lb1 = '====================================================='
lb2 = '+++++++++++++++++++++++++++++++++++++++++++++++++++++'
# print title of text6
print(text6)

# print concordance of 'monstrous' from Moby Dick
print(text1.concordance('monstrous'))

# explore other concordances in different texts
print(text6.concordance('rabbit'))
print(lb1)
print(text3.concordance('lived'))
print(lb2)
print(text5.concordance('fuck'))

# print similarities to monstrous in Moby Dick and S & S
print(text1.similar('monstrous'))
print(lb1)
print(text2.similar('monstrous'))
print(lb2)

# print common contexts for very and monstrous in S & S
print(text2.common_contexts(['monstrous', 'very']))
print(lb1)

# explore similar and common_contexts
print(text6.similar('king'))
print(lb2)
print(text3.similar('king'))
print(lb1)
print(text5.common_contexts(['love', 'fuck']))
