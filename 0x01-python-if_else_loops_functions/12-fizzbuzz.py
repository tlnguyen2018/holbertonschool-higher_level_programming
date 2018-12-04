#!/usr/bin/python3
def fizzbuzz():
    i = 1
    while (i <= 100):
        if i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        elif i % 15 == 0:
            print("FizzBuzz", end=" ")
        else:
            print("{}".format(i), end=" ")
        i = i + 1
