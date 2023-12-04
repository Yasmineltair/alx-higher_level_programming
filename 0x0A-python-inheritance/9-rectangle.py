#!/usr/bin/python3
BaseGeometry = __import__('8-base_geometry').BaseGeometry
""" module contains class BaseGeometry"""


class Rectangle(BaseGeometry):
    """ class Rectangle """

    def __init__(self, width, height):
        """ instante method """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ area method """

        return self.__width * self.__height

    def __str__(self):
        """ str method """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
