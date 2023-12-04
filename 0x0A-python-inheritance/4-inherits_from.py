#!/usr/bin/python3
""" module that has inherits_from method"""


def inherits_from(obj, a_class):
    """ function that returns True if the object
    is an instance of a class that inherited """

    return True if isinstance(obj, a_class) else type(obj)
