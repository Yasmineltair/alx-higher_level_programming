#!/usr/bin/python3
""" function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    row_check = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for number in row:
            if type(number) is not int and type(number) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of"
                    "integers/floats")
            if row_check == 0:
                row_check = len(row)
            elif row_check != len(row):
                raise TypeError(
                    "Each row of the matrix must have the same size")
        if type(div) is not int and type(div) is not float:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        return [[round(number / div, 2) for number in row] for row in matrix]
