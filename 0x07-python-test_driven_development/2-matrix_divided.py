#!/usr/bin/python3
"""
function that divide a matrix
Return the value in each element of the matrix
"""


def matrix_divided(matrix, div):
    """ Function that divide a matrix """
    divd = []
    esize = "Each row of the matrix must have the same size"
    etype = "matrix must be a matrix (list of lists) of integers/floats"
    rowb = len(matrix[0])

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        divd.append([])
        if(len(matrix[i]) is not rowb):
            raise TypeError(esize)
        for j in range(len(matrix[i])):
            if type(matrix[i][j] not in [int, float]:
                raise TypeError(etype)
            divd[i].append(round(matrix[i][j] / div, 2))
            rowb = len(matrix[i])
    return divd
