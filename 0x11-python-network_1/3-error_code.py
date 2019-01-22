#!/usr/bin/python3
"""Sends a POST to passed URL with an email parameter
"""


import urllib.request
from sys import argv

if __name__ == "__main__":
    try:
        dest = urllib.request.Request(argv[1])
        with urllib.request.urlopen(dest) as resp:
            print(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print('Error code: ' + str(e.code))
