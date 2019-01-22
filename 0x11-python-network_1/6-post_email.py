#!/usr/bin/python3
"""POSTs an email
"""


import requests
from sys import argv

if __name__ == "__main__":
    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.content.decode('utf-8'))
