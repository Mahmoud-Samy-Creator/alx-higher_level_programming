#!/usr/bin/python3
# A script fetches url 'https://alx-intranet.hbtn.io/status'

import urllib.request

# URL to be fetched
url = 'https://alx-intranet.hbtn.io/status'

req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    data = response.read()

print("Body response:")
print(f"\t- type: {type(data)}")
print(f"\t- content: {data}")
print(f"\t- utf8 content: {data.decode('utf-8')}")
