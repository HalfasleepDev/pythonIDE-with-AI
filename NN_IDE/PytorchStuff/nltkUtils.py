import nltk
#nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
import numpy as np

stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bagOfWords(tokenizedSentence, allWords):
    tokenizedSentence = [stem(w) for w in tokenizedSentence]

    bag = np.zeros(len(allWords), dtype=np.float32)
    for idx, w, in enumerate(allWords):
        if w in tokenizedSentence:
            bag[idx] = 1.0

    return bag


#a = "Hello world!"
#print(a)
#a = tokenize(a)
#print(a)