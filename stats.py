# creating a frequency distribution of each adjectives.
all_words = nltk.FreqDist(all_words)
# listing the 5000 most frequent words
word_features = list(all_words.keys())[:5000]
