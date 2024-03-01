#!/usr/bin/python3
""" module documentation"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    result = requests.get(url)
    data = result.text
    resType = type(data)
    print(f"Body response:\n\t- type: {resType}\n\t\
- content: {data}")
