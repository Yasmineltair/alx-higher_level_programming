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
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ static method that that returns the JSON
        string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file:"""
        list = []
        if list_objs is not None:
            list = [objectives.to_dictionary() for objectives in list_objs]
        with open("{}.json".format(cls.__name__), "w") as file:
            file.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string:"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)
