from nltk.book import *

# print title of text6
print(text6)

# print concordance of 'monstrous' from Moby Dick
print(text1.concordance('monstrous'))

# explore other concordances in different texts
print(text6.concordance('rabbit'))
print('====================================================')
print(text3.concordance('lived'))
print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(text5.concordance('fuck'))
