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

    @property
    def width(self):
        """ width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ area method """
        return self.__width * self.height

    def display(self):
        """ display public method """
        [print() for space in range(self.y)]
        [print(" " * self.x + "#" * self.width)
         for line in range(self.height)]

    def __str__(self):
        """ str method """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """ public method that assigns a key/value argument to attributes:"""
        indx = 0
        if args is not None and len(args) != 0:
            for i in args:
                indx += 1
                if indx == 1:
                    self.id = i
                elif indx == 2:
                    self.__width = i
                elif indx == 3:
                    self.__height = i
                elif indx == 4:
                    self.__x = i
                elif indx == 5:
                    self.__y = i
        else:
            for key, values in kwargs.items():
                setattr(self, key, values)

    def to_dictionary(self):
        """ public method that returns the
        dictionary representation of a Rectangle"""
        dictionary = {}
        for i in ["id", "width", "height", "x", "y"]:
            dictionary[i] = getattr(self, i)
        return dictionary
