#!/usr/bin/python3
"""Sends a POST to passed URL with an email parameter
"""


import urllib.parse
import urllib.request
from sys import argv

if __name__ == "__main__":
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as resp:
        page = resp.read()
    print(page.decode("utf-8"))
