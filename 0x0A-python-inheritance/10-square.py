#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
""" module contains class square"""


class Square(Rectangle):
    """ square class"""

    def __init__(self, size):
        """ initialization"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        "area"

        return self.__size ** 2
