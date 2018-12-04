#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            j = chr(ord(i) - 32)
            print("{}".format(j), end="")
    print("")
