#!/usr/bin/python3
""" module has class  Class to JSON"""


def class_to_json(obj):
    """ unction that returns the dictionary
    description with simple data structure """
    return vars(obj)
