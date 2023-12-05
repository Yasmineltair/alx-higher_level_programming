#!/usr/bin/python3
""" module to read file"""


def read_file(filename=""):
    """ function that reads a text file """
    with open(filename, "r", encoding="UTF-8") as file:
        print(file.read(), end="")
