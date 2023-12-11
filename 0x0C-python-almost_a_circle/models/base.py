#!/usr/bin/python3
""" module that has class Base"""
import json
import os.path


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor"""

        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
