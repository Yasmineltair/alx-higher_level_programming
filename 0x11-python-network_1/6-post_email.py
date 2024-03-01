#!/usr/bin/python3
""" module documentation """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    params = {"email": email}
    result = requests.post(url, data=params)
    print(result.text)
