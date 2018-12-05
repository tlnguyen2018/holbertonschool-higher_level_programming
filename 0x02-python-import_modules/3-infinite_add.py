#!/usr/bin/python3


def main():
    import sys
    sum = 0
    for value in sys.argv[1:]:
        sum = sum + int(value)
    print("{:d}".format(sum))
if (__name__ == "__main__"):
    main()
