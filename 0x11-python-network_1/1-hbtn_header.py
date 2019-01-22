#!/usr/bin/python3
"""Displays X-Request-Id value of header response from passed URL
"""


import urllib.request
from sys import argv

if __name__ == "__main__":
    dest = urllib.request.Request(argv[1])
    with urllib.request.urlopen(dest) as resp:
        head = resp.info()
        hl = str(head).split("\n")
        for header in hl:
            if "X-Request-Id" in header:
                print(header.split(": ")[1])
