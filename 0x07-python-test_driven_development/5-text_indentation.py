#!/usr/bin/python3
""" function that prints a text with 2 new lines
 after each of these characters: ., ? and :"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    for delim in ".:?":
        text = (delim + "\n\n").join([line.strip(" ") for line in text.split(delim)])
    print("{}".format(text), end="")
