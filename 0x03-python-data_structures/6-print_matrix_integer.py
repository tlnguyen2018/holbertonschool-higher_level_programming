#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    numstring = ''
    for row in matrix:
        numstring += "\n"
        for number in row:
            numstring += "{:d} ".format(number)
        numstring = numstring[:-1]
    print(numstring[1:])
