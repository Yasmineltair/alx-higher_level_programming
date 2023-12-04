#!/usr/bin/python3
""" module that has inherits_from method"""


def inherits_from(obj, a_class):
    """ function that returns True if the object
    is an instance of a class that inherited """

    return False if type(obj) is a_class else isinstance(obj, a_class)
