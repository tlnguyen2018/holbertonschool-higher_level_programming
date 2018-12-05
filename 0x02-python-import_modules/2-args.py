#!/usr/bin/python3


def main():
    import sys
    if (len(sys.argv) == 1):
        print("0 arguments.")
        exit()
    elif (len(sys.argv) == 2):
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    i = 1
    for value in sys.argv[1:]:
        print("{:}: {}".format(i, value))
        i = i + 1
if (__name__ == "__main__"):
    main()
