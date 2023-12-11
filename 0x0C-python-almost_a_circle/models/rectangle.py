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

    @width.getter
    def width(self):
        """ width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError(f"{value} must be an integer")
        elif value <= 0:
            raise ValueError(f"{value} must be > 0")
        else:
            self.__width = value

    @height.getter
    def height(self):
        """ height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError(f"{value} must be an integer")
        elif value <= 0:
            raise ValueError(f"{value} must be > 0")
        else:
            self.__height = value

    @x.getter
    def x(self):
        """ x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError(f"{value} must be an integer")
        elif value < 0:
            raise ValueError(f"{value} must be >= 0")
        else:
            self.__x = value

    @y.getter
    def y(self):
        """ y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError(f"{value} must be an integer")
        elif value < 0:
            raise ValueError(f"{value} must be >= 0")
        else:
            self.__y = value
