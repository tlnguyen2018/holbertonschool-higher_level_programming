#!/usr/bin/python3
from sys import argv


if len(argv) == 1:
    print("0 arguments.")
    exit()
elif len(argv) == 2:
    print("1 argument:")
else:
    print("{} arguments:".format(len(argv) -1))
i = 1
for value in argv[1:]:
    print("{:d}: {}".format(i, value))
    i = i + 1
