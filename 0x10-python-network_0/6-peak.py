#!/usr/bin/python3
""" module documentation"""


def find_peak(list_of_integers):
    """ function find peak"""
    if list_of_integers:
        lf = 0
        r = len(list_of_integers) - 1
        while lf < r:
            mid = (lf + r) // 2
            if list_of_integers[mid] > list_of_integers[mid + 1]:
                r = mid
            else:
                lf = mid + 1
        return list_of_integers[lf]
