#!/usr/bin/python3
""" contain json function"""

import json
""" import json """


def from_json_string(my_str):
    """function that returns he JSON representation of an object(string)"""
    return json.loads(my_str)
