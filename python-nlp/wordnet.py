import os
import nltk
from nltk.corpus import wordnet as wn


# smoke test - seeing what comes up when you print commands w/ a test word ("drain")
wn.synset('net.v.02').lemmas()
for synset in wn.synsets('drain'):
    print(synset.lemma_names(), len(synset.lemma_names()))

# adapting filepath stuff
cwd = os.getcwd()
print(cwd)

os.listdir(cwd)
coll = os.path.join(cwd, 'computer') #note to self: 'computer' is the directory the scraper dumped the files into
print(os.listdir(coll))

#making a single corpus - note to self: this format only gets .txt files - good for testing because of the irregular
#filetypes present in the scraping set
for file in os.listdir(coll):
   if file.endswith(".txt"):
        filepath = f"{coll}/{file}"
        print(filepath)

from nltk.corpus import PlaintextCorpusReader
corpus_root = 'computer'
corpus = PlaintextCorpusReader(corpus_root, '.*')

#SMOKE TEST - making sure they're reading
print(corpus.fileids()) #follows format ['blah.txt', 'blah.txt'...]
print(corpus.words('ad.txt'))

# tokenizing
tokenized = corpus.words('codegeek.txt')
# i found that corpus.words() to get all doesn't work - based on the error, i think there's some unicode that isn't recognized by utf-8?
# everything in codegeek.txt is recognized, hence why it is my example here.

print("")
print("")
print(nltk.pos_tag(tokenized)) # reference
print("")
print("!!! Retrieval Stage !!!")


isnoun = lambda pos: pos[:2] == 'NN'
nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if isnoun(pos)]
print(set(nouns))
##note to self: NNP is how singular proper nouns are tagged in (word, pos) format

freq = nltk.FreqDist(nouns)
print("Ten most common nouns in codegeek.txt:")
freqcom = freq.most_common(10)
print(freqcom)
print("Similar words to the previous ten:")

for (word, num) in freqcom:
    print(wn.synonyms(word))
    # doesn't work exactly because it doesn't differentiate cases plurals/singulars, and some things that are noted as nouns aren't real
    #with some filtering it probably could, though