#!/usr/bin/python3
"""POSTs a letter
"""


import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        argv.append("")
    dest = 'http://0.0.0.0:5000/search_user'
    r = requests.post(dest, data={'q': argv[1]})
    try:
        r.json()
    except Exception:
        print('Not a valid JSON')
    else:
        if not r.json():
            print('No result')
        else:
            print("[{}] {}".format(r.json()['id'], r.json()['name']))
