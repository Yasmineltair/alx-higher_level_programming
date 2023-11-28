#!/usr/bin/python3
""" a class LockedClass with no class or object attribute, """


class LockedClass:
    """
    prevents the user from dynamically creating
    new instance attributes, except if the new
    instance attribute is called first_name
    """

    __slots__ = ["first_name"]

    def __init(self, first_name=""):
        self.first_name = first_name
