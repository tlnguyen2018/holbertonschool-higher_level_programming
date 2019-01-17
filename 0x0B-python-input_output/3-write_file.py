#!/usr/bin/python3
"""
Write string to text file
"""


def write_file(filename="", text=""):
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
