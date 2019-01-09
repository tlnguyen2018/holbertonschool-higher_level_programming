#!/usr/bin/python3
"""
Write a function that prints a text with 2 new lines
after each of these characters: ., ? and :

Prototype: def text_indentation(text):
text must be a string, otherwise raise a TypeError exception with the message
text must be a string
There should be no space at the beginning or at the end of each printed line
"""


def text_indentation(text):
    if not isinstance(text, str) or text is None:
        raise TypeError("text must be a string")
    text = text.strip( ' ' )
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')
    print(text)
