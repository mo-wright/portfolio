import sys
print(sys.executable)

for line in open("disneySongLyrics.txt"):
    for word in line.split():
       if word.endswith('ing'):
            print(word)
