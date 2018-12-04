#!/usr/bin/python3
def fizzbuzz():
    while (i <= 100):
        if i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        elif i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i == 100:
            print("Buzz", end="")
        else:
            print("{}".format(i), end=" ")
