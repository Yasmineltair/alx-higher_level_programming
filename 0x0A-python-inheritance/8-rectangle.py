#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" module that have class BaseGeometry"""


class BaseGeometry:
    """ class BaseGeometry"""

    def area(self):
        """ public instance"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ public instance method """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """  class Rectangle that inherits from BaseGeometry """

    def __init__(self, width, height):
        """ Instantiation with width and height """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
