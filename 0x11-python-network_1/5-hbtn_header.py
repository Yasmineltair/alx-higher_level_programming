#!/usr/bin/python3
""" module documentation"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    result = requests.get(url)
    print(result.headers.get("X-Request-Id"))
