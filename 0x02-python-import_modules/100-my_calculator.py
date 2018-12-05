#!/usr/bin/python3


def main():
    from calculator_1 import add, sub, mul, div
    import sys
    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    o = sys.argv[2]
    if (o != '+' and o != '-' and o != '*' and o != '/'):
        print("Unknown operator. Only: +, -, * and / available")
        exit(1)
    if (sys.argv[2] == '+'):
        result = add(int(sys.argv[1]), int(sys.argv[3]))
    if (sys.argv[2] == '-'):
        result = sub(int(sys.argv[1]), int(sys.argv[3]))
    if (sys.argv[2] == '/'):
        result = div(int(sys.argv[1]), int(sys.argv[3]))
    if (sys.argv[2] == '*'):
        result = mul(int(sys.argv[1]), int(sys.argv[3]))
    print("{} {} {} = {}".format(sys.argv[1], sys.argv[2],
                                 sys.argv[3], result))

if (__name__ == "__main__"):
    main()
