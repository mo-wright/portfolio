## Beginning Stages:

Found ``(?<=\n\n).*?(?=\n\n)``. Replaced with ``<sp>\0</sp>`` to separate each chunk between new lines.

Wrapped the entire document in a root ``<xml></xml>`` tag to create well-formed XML.