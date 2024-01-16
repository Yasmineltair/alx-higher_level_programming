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

    def __str__(self):
        """ str method """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """ public method that assigns attributes:"""
        indx = 0
        if args is not None and len(args) != 0:
            for i in args:
                indx += 1
                if indx == 1:
                    self.id = i
                elif indx == 2:
                    self.size = i
                elif indx == 3:
                    self.x = i
                elif indx == 4:
                    self.y = i
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ public method returns the dictionary representation of a Square:"""
        dictionary = {}
        for i in ["id", "size", "x", "y"]:
            dictionary[i] = getattr(self, i)
        return dictionary
