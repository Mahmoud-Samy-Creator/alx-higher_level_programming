#!/usr/bin/python3
# Send request to url, display value of header

import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        print(response.info().get("X-Request-Id"))

"""
info - this returns a dictionary-like object
that describes the page fetched,
particularly the headers sent by the server.
It is currently an http.client.HTTPMessage instance.

Usage: responce.info().get("Key")
"""
