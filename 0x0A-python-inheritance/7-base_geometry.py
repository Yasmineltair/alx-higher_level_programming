#!/usr/bin/python3
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
