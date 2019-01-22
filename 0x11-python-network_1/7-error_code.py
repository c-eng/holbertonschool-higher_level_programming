#!/usr/bin/python3
"""display http status code
"""


import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print('Error code: ' + str(r.status_code))
    else:
        print(r._content.decode('utf-8'))
