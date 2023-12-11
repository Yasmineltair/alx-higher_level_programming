#!/usr/bin/python3
""" module that contain class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
