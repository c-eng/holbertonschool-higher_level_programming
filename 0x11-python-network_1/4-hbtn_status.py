#!/usr/bin/python3
"""Sends a POST to passed URL with an email parameter
"""


import requests

if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: ' + str(type(r.text)))
    print('\t- content: ' + str(r._content.decode('utf-8')))
