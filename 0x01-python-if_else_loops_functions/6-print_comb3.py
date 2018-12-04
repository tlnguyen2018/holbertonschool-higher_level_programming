#!/usr/bin/python3
for first in range(10):
    for second in range(10):
        if second > first:
            print("{}".format(first), end='')
            if first != 8 or second != 9:
                print("{}".format(second), end=', ')
            else:
                print("{}".format(second))
