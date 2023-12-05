#!/usr/bin/python3
""" contain json function"""

import json
""" import json"""
import os.path
""" import os.path"""
import sys
""" import sys"""
from sys import argv
""" import argv"""

save_to_json_file = __import__(5-save_to_json_file).save_to_json_file
load_from_json_file = __import__(6-load_from_json_file).load_from_json_file

filename = "add_item.json"
json_list = []

if os.path.exits(filename):
    json_list = load_from_json_file(filename)

for i in argv[1:]:
    json_list.append(i)

save_to_json_file(json_list, filename)
