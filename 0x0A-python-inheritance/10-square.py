#!/usr/bin/python3
""" module contains class square"""


class BaseGeometry:
    """ class BaseGeometry"""

    def area(self):
        """ public instance"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ public instance method """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
