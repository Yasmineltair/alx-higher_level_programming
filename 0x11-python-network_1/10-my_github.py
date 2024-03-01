#!/usr/bin/python3
""" module documentation"""
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    headers = {'Authorization': f'Bearer {password}'}
    result = requests.get("https://api.github.com/user", headers=headers)
    if (result.status_code >= 400):
        print("None")
        exit()
    print(result.json()["id"])
