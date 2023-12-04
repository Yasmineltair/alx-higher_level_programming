#!/usr/bin/python3
""" module with class list """

class MyList(list):
    """ class list inherted frmo list"""
    pass

    def print_sorted(self):
        """ Public instance method """
        print (sorted(list(self)))
