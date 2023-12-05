#!/usr/bin/python3
""" Pascal's Triangle module"""


def pascal_triangle(n):
    """ eturns a list of lists of integers
    representing the Pascal’s triangle"""
    lst = []
    if n <= 0:
        return lst
    for rw in range(n):
        for cn in range(rw + 1):
            if cn == 0:
                lst.append([1])
            elif cn == rw:
                lst[rw.append(1)]
            else:
                lst[rw].append(lst[rw - 1][cn] + lst[rw - 1][cn - 1])
    return lst
