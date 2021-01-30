import nltk
#from nltk.corpus import twitter_samples as ts


#================================== POS ===========

text1 = nltk.word_tokenize("I left the room")
text2 = nltk.word_tokenize("Left of the room")

p1 = nltk.pos_tag(text1, tagset='universal')
p2 = nltk.pos_tag(text2, tagset='universal')

print(p1)
print(p2)


