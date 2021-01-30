import nltk

example_sent = nltk.word_tokenize("The company is located in South Africa")
print(example_sent)

tagged_sent = nltk.pos_tag(example_sent)
print(tagged_sent)

print(nltk.ne_chunk(tagged_sent))


