#!/usr/bin/python3


def main():
    import hidden_4
    for i in dir(hidden_4):
        if i[0] != "_":
            print(i)
if __name__ == "__main__":
    main()
