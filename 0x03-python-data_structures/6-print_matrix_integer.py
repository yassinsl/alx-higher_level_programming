#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for colmn in row:
            print("{:d}".format(colmn), end=" ")
        print()
