#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
<<<<<<< HEAD
            i = chr(ord(i) - 32)
            print("{:}".format(i), end="")
=======
            j = chr(ord(i) - 32)
            print("{}".format(j), end="")
>>>>>>> ca66a8aa52c930a3cfb887329f625a6273124610
    print("")
