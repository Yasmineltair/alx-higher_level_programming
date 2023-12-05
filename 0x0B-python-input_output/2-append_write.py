#!/usr/bin/python3
""" module to append in file"""


def append_write(filename="", text=""):
    """ function that append a string to a text file """
    with open(filename, "a", encoding="UTF-8") as file:
        return file.write(text)
