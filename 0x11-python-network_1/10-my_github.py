#!/usr/bin/python3
"""gets Github id
"""


import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 3:
        argv.append("")
    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(r.json().get('id'))
