#!/usr/bin/python3
""" module with method is_same_class"""


def is_same_class(obj, a_class):
    """ function that returns True if the object
      is exactly an instance"""

    return type(obj) is a_class
