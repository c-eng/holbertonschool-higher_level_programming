#!/usr/bin/python3
"""searches on the Star Wars API
"""


import requests
from sys import argv

if __name__ == "__main__":
    qry = {'search': argv[1]}
    r = requests.get('https://swapi.co/api/people/', params=qry)
    jason = r.json()
    num = jason['count']
    print('Number of results: {}'.format(num))
    for elm in jason['results']:
        print(elm['name'])
