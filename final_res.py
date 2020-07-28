classifier = nltk.NaiveBayesClassifier.train(training_set)
t=(nltk.classify.accuracy(classifier, testing_set))*100
y.append(t)
print("Classifier accuracy percent:",t)
classifier.show_most_informative_features(15)
