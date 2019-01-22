#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status
"""


import urllib.request

dest = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(dest) as resp:
    page = resp.read()
print('Body response:')
print('    - type: ' + str(type(page)))
print('    - content: ' + str(page))
print('    - utf8 content: ' + str(page.decode("utf-8")))
