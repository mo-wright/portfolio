Runtime
Find: ``\t(\d*) (min)``
Replace: ``<runTime unit="\2">\</runtime>``

Year
Find: ``(</title>)(\d{4})(\t)``
Replace ``\1<year>\2</year>``
	Note: I forgot the ``\1`` here initally and had to use find: ``(?<=<title>)(.*)(?=<year>)`` and replace: ``$1</title>`` to fix it

Country
Find: ``(?<=</year>)(.*)(?=<r)``
Replace: ``<country>$1</country>``

Country, accounting for movies with missing runtime data (around 479 found items)
Find:``(?<=</year>)(.*)(?=</movie>)``
Replace:``<country>$1</country>``

....Then, I found that this didn't fix the tagging issue w/ countries that spread across multiple lines (as I had already used the "pretty printing" to check out my work), so I used a combination of ``(?<=</year>)((.|\n)*)(?=<r)`` and ``(?<=</year>)"[\s\S]*?"`` to account for *that*.
