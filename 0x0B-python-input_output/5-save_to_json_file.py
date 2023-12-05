#!/usr/bin/python3
""" contain json function"""

import json
""" import json """


def save_to_json_file(my_obj, filename):
    """ unction that writes an Object to a text file"""
    with open(filename, "w", encoding="UTF-8") as file:
        json.dump(my_obj, file)
