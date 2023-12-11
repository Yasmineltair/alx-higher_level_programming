#!/usr/bin/python3
""" module square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherts frmo Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """ size setter"""
        self.width = value
        self.height = value
