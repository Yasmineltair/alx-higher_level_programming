#!/usr/bin/python3
"""Defines a class square."""


class Square:
    """Defines a square by:(based on 1-square.py)
    attributes
    size: size of the square
    """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
