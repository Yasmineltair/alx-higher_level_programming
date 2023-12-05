#!/usr/bin/python3
""" contain json function"""

import json
""" import json """


def load_from_json_file(filename):
    """  function that creates an Object from a “JSON file”:"""
    with open(filename, "r", encodeing="UTF-8") as file:
        return json.load(file)
