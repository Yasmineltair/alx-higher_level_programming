#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxvalue = 0
    maxkey = None
    for k, v in a_dictionary.items():
        if v > maxvalue:
            maxvalue = v
            maxkey = k
    return maxkey
