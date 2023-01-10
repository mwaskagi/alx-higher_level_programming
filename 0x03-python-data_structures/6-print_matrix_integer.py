#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None or matrix == [[]]:
        print()
    for a in matrix:
        b = 1
        for c in a:
            if b < len(a):
                print("{:d} ".format(j), end="")
            else:
                print("{:d}".format(c))
            b += 1
