#!/usr/bin/python3
""" define rectangle"""


class Rectangle:
    """ define rectangle"""

    def __init__(self, width=0, height=0):
        """ init of class Rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ set the rectangle width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ set the rectangle height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return rectangle area"""

        return self.__height * self.__width

    def perimeter(self):
        """ return rectangle perimeter """

        if self.__height == 0 or self.__width == 0:
            return
        return (self.__height * 2) + (self.__width * 2)
