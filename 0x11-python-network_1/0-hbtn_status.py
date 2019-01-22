#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status
"""


import urllib.request

dest = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(dest) as resp:
    page = resp.read()
print('Body response:')
print('\t- type: ' + str(type(page)))
print('\t- content: ' + str(page))
print('\t- utf8 content: ' + str(page.decode("utf-8")))
