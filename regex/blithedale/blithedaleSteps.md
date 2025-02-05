## Preliminary
1. Searched for `&`, `<`, and `>`, but did not find any within the text - nothing had to be changed here.
2. Found `\n{3,}` and replaced it with `\n\n` to remove extra spaces.

## XML Organization 
3. This may seem like a weird place to start, but I began with the Chapter Titles for ease of Chapter divisions themselves. Found `^\w*[IVXLC]\. .*`, which located any Roman numeral followed by a period beginning a line plus the rest of the line, and encapsulated them in a title tag by replacing them with `<title>\0</title>`

4. Found everything from the first `<title>` tag (inclusive) until the next `<title>` tag (exclusive) using `<title>.*?(?=<title>)`. I normally would do two exclusive markers, with the first finding a title end tag and the second finding a title beginning tag, but the example included the title nested within the chapter tags. This accomplishes that. I encapsulated the found chapter by using the replace `<chapter>\0</chapter>\n`. The newline is included for organizational purposes.
	1. This did not include the final chapter because there is no "next" title begin tag. I went ahead and grabbed it with `(?<=</chapter>\n)<title>.*?(?=\z)` and used `<chapter>\0</chapter>` to tag it. I didn't feel the need for the new line since it took us to the end of the document.

5. I then used `(?<=\n{2}).*?(?=\n{2})` to find every chunk of text between a series of two line breaks, which caught every paragraph (as well as every chunk denoting chapter beginnings, ends, and entire titles - but this is an easy fix). Replaced them using `<p>\0</p>` for now.

## Cleanup

1. A bit of recursion happened in the last step, so I searched for `<p><` to find where empty `<p>` tags were formed. I replaced them with simply `<`.
	1. This half-fixed the Title issue with paragraph tags, so I went ahead and replaced `</title></p>` with just `<title>` to complete that.
	2. Alongside this, I searched for duplicate tags such as `</p></p>` and replaced them with a singular. (`</p>`) in this example.
		1. For consecutive `</chapter>` tags, I did it myself, since I didn't really want to fiddle with regex there. Sorry!

2. At this point, there were still some random issues in a bunch of places and I began testing the .txt file against the .xml file. Here, I added the `<xml>` tags manually.

3. I used `(?<=<chapter>).*?(?=<chapter>)` and shuffled through to find sections that did not resolve with a `</chapter>` tag. I added the `</chapter>` tag when applicable.

4. From here I just had to fix up the beginning data. I wrapped the title in a `<titleBook>` element, Hawthorne's name in an `<author>` element, and the entirety of the Table of Contents in a `<toc>` element. I then used `^ \s{0,}( .*)` to grab all of the chapter names in the `<toc>` element and used `<tocTitle>\1</tocTitle>` to wrap them. I did Chapter 27 individually as not to complicate things with the weird spacing.