#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    n = number % 10
else:
    n = (number * -1) % 10
if n > 5:
    print("Last digit of {:d}".format(number), "is {:d} and is greater than 5".
          format(n))
elif n == 0:
    print("Last digit of {:d}".format(number), "is {:d} and is 0".
          format(n))
else:
    print("Last digit of {:d}".
          format(number), "is {:d} and is less than 6 and not 0".format(n))
