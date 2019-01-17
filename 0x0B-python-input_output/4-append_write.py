#!/usr/bin/python3
"""
Append string to text file
"""


def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
