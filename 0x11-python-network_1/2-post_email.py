#!/usr/bin/python3
""" documentation for module"""
import urllib.request
import sys
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    params = {"email": email}
    utf_params = urllib.parse.urlencode(params).encode('utf-8')
    req = urllib.request.Request(url, data=utf_params, method='POST')
    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
