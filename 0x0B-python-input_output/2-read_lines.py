#!/usr/bin/python3
"""
Fuction that print the n line of text
"""


def read_lines(filename="", nb_lines=0):
    count_line = 0
    with open(filename, encoding="utf-8") as f:
        for line in f:
            if (count_line < nb_lines) or nb_lines == 0 or nb_lines < 0:
                print(line, end="")
            count_line += 1
