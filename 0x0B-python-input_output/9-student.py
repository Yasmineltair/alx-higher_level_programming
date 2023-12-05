#!/usr/bin/python3
""" module contains class Student"""


class Student:
    """ class Student"""

    def __init__(self, first_name, last_name, age):
        """ init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ public method"""
        return self.__dict__
