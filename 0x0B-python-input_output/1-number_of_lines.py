#!/usr/bin/python3
"""
Fucntion return number of line of textfile
"""


def number_of_lines(filename=""):
    with open(filename, encoding="UTF8") as f:
        return (len(f.readlines()))
