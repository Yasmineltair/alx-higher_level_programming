#!/usr/bin/python3
""" defines rectangle class """


class Rectangle:
    """ define rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ init of class Rectangle """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ print rectangle """
        if self.__width == 0 or self.__height == 0:
            return ""
        rec_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += str(Rectangle.print_symbol)
            rec_str += "\n"
        return rec_str[:-1]

    @property
    def width(self):
        """ width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ set the rectangle width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ set the rectangle height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return rectangle area"""

        return self.__height * self.__width

    def perimeter(self):
        """ return rectangle perimeter """

        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __repr__(self):
        """return a string representation of the rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ print message for delete rectangle class """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
