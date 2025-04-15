import pygal
import spacy
from spacyTest import nouns
from pygal.style import RedBlueStyle
import pandas as pd
import os

## Bar Chart Creation

nlp = spacy.load("en_core_web_md")

filepath = 'computer/anonymit'
f = open(filepath, 'r', encoding='utf8').read()

bar_chart = pygal.Bar(style=RedBlueStyle)
bar_chart.title = 'Top 20 Most Frequent Nouns in An Example Text File'

for word, freq in nouns:
    bar_chart.add(word, freq)

bar_chart.render_to_file('top20_nouns.svg')

# TSV

collPath = 'computer'

def wordCollector(words, unit):
    wordList = []
    nodeAtts = []
    unitList = []
    for token in words:
        if token.pos_ == "NOUN":
            wordList.append(token.lemma_)
            nodeAtts.append(token.pos_)
            unitList.append(unit)

    data = {
        'word': wordList,
        'nodeType': nodeAtts,
        'unit': unitList
    }
    df = pd.DataFrame(data)
    return df
    # This is returning a separate dataframe for every source text file.

# We need to consolidate all the dataframes into one file. Collect all dataframes here!
allDataFrames = []

for file in os.listdir(collPath):
    if file.endswith(".txt"):
        filepath = f"{collPath}/{file}"
        name, extension = os.path.splitext(file)
        with open(filepath, 'r', encoding='utf8') as f:
            readFile = f.read()
            spacyRead = nlp(readFile)
            myDataFrame = wordCollector(spacyRead, name)
            # Add each individual dataframe as it comes out into the list of dataframes!
            allDataFrames.append(myDataFrame)

# Make an output filepath
outputFilePath = 'networkData.tsv'
# Turn the list of dataframes into one dataframe:
fullDataFrame = pd.concat(allDataFrames, ignore_index=True)

fullDataFrame.to_csv(outputFilePath, sep='\t', index=False)
print('I just saved a dataframe as a TSV file.')
# Go check your filestash for the file.