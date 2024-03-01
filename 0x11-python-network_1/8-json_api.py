#!/usr/bin/python3
""" module documentation"""
import requests
import sys


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    pyload = {"q": letter}
 
    result = requests.post("http://0.0.0.0:5000/search_user", data=pyload)
    try:
        response = result.json()
        if response == {}:
            print("No result")
	else:
	    print ("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
            print("Not a valid JSON")
