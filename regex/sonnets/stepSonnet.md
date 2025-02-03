# Sonnet txt to XML steps
## Beginning Cleanup ##

1. I began with ``^ +`` to get rid of the spaces that opened each line.
2. I went through the standard replace ``&`` with ``&amp;``course alongside the ``<`` and ``>`` equivalents, but for this file it wasn't necessary - they didn't appear anywhere.

## Line Tags ##

1. Used ``(\w.+)`` to locate every entire line. Replaced them with ``<line>\1</line>`` to encapsulate them into a tag. Generally an imperfect start but is later fixed.

## Sonnet Tags ##

1. Began with the Roman numerals that wouldn't be caught by Step 1 of the line tags. Used ``(\n[IVXLC)])`` (single Roman numeral instances on a new line) to find them, replaced with ``<sonnet number="\1">``
	1. This leaves an incomplete tag that is resolved in Step 3.
2. Then went on to Roman numerals that would have been given the line tag. Used ``<line>(\w+[IVXLC)])</line>`` to find them and ``<sonnet number="\1">`` as the replacement.
	1. Still leaves an incomplete tag, but is resolved in Step 3.
3. Used ``(</line>\n{2,4})`` to find incomplete Sonnet tags using the standard spacing within the document. Replaced with ``\1</sonnet>`` to complete the tags. This puts it on the same line as the next Sonnet's beginning tag.
	1. Some sonnets didn't follow the same spacing pattern, resolved in Step 4.
	2. Caused erroneous ``</sonnet>`` tags near the beginning, resolved in Closing Cleanup Step
4. Used ``(</line>\n{1})(<s)`` used to find the leftover sonnets without end tags. Replaced with ``\1</sonnet>\2``.

## Closing Cleanup

1. Replaced ``<<`` with `<` across the document because that happened somewhere, affecting two tags.
2. Changed ``</line></line>`` to ``</line>``, and ``</sonnet></sonnet>`` to ``</sonnet>``, accounting for accidental duplicates. As far as I could tell, no other duplicates were created.
3. Removed erroneous ``</sonnet>`` end tags on the beginning.
	1. I didn't remove the Gutenberg information (Shakespeare's name, etc.) when I began the regex-ing. I did that at this point, since it wasn't necessary in this project. You could probably remove that as one of the Opening Cleanup steps, but I didn't, so it may affect the workflow shown in this document.
4. Ctrl + A, Ctrl + E, wrapped the whole document in an ``<xml>`` tag.



