import spacy
import os
from collections import Counter

nlp = spacy.load("en_core_web_md")
remoteWeird = 'remoteWeird'

# Getting files

def readTextFiles(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        readFile = f.read()
        stringFile = str(readFile)
        lengthFile = len(readFile)
        # (Literally, we'll just count the number of characters in this.)
        print(lengthFile)

for file in os.listdir(remoteWeird):
    if file.endswith(".txt"):
        filepath = f"{remoteWeird}/{file}"
        print(filepath)
        readTextFiles(filepath)

# Doing stuff

def readTextFiles(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        readFile = f.read()
        stringFile = str(readFile)

        tokens = nlp(stringFile)
        wordOfInterest = nlp(u'terror') #PREVIOUSLY: Eldritch,

        highSimilarityDict = {}
        highSimilarityDict = {}
        sorted_similarity = sorted(highSimilarityDict.items(), key=lambda item: item[1], reverse=True)
        wordCounts = Counter()

        for token in tokens:
            if token and token.vector_norm:
                if wordOfInterest.similarity(token) > .5:
                    wordCounts[token.text] += 1
                    highSimilarityDict[token] = wordOfInterest.similarity(token)
                    # The line above creates the structure for each entry in my dictionary.
        print(f'This is a dictionary of words most similar to the word "{wordOfInterest.text}" in "{file}".')
        for word, similarity in highSimilarityDict.items():
            count = wordCounts[word.text]
            print(f"{word}: similarity={similarity:.3f}, count={count}")
        print('\n')

for file in os.listdir(remoteWeird):
    if file.endswith(".txt"):
        filepath = f"{remoteWeird}/{file}"
        readTextFiles(filepath)





