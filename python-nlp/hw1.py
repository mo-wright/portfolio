import nltk
from nltk import FreqDist, RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
# this gets rid of punctuation in the 'mostcommon' command -- really annoying!

# getting the txt files usable (i read ahead for this)
with open('poeWorks.txt', 'r', encoding='utf8') as file:
    string = file.read()
poeToken = tokenizer.tokenize(string)
poe = nltk.Text(poeToken)

with open('loveCraftWorks.txt', 'r', encoding='utf8') as file:
    string = file.read()
loveToken = tokenizer.tokenize(string)
love = nltk.Text(loveToken)

# general testing to make sure commands can be run
print("Poe's")
poe.collocations()
print("Lovecraft's")
love.collocations()

# frequent words (excluding stop words)
print("")
stopWords = nltk.corpus.stopwords.words('english')
stopSortPoe = [w for w in poeToken if w.lower() not in stopWords]
stopSortLove = [w for w in loveToken if w.lower() not in stopWords]

print("Frequent Words (Poe)")
print(FreqDist(stopSortPoe).most_common(15))
print("Frequent Words (Lovecraft)")
print(FreqDist(stopSortLove).most_common(15))

# similar words
print("")
print("Similar to 'Could' (Poe)")
poe.similar("could")
print("Similar to 'Could' (Lovecraft)")
love.similar("could")
