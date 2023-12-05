#!/usr/bin/python3
""" module to write in file"""


def write_file(filename="", text=""):
    """ function that writes a string to a text file """
    with open(filename, "w", encoding="UTF-8") as file:
        return file.write(text)
