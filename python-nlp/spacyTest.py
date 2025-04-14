import spacy
from collections import Counter

nlp = spacy.load("en_core_web_md")

filepath = 'computer/anonymit'
f = open(filepath, 'r', encoding='utf8').read()

spacyRead = nlp(f)
#for token in spacyRead:
    #print(token.text, "---->", token.pos_, ":::::", token.lemma_)

def wordCollector(words):
    wordList = []
    count = 0
    for token in words:
        if token.pos_ == "NOUN":
            count += 1
            wordList.append(token.lemma_)
    return wordList

myWords = wordCollector(spacyRead)

counts = Counter(myWords)
nouns = counts.most_common(20)
o = open("twentyNouns.txt", "w")

for r in nouns:
    o.write(str(r) + "\n")
