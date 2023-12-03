#!/usr/bin/python3
"""
Takes in url, email, sends a request, print the error code,
handle urllib.error.HTTPError
"""

if __name__ == "__main__":
    from urllib import request, error
    from sys import argv

    # Get url
    url = argv[1]

    # Reciving response
    try:
        with request.Request(url) as responce:
            print(responce.read().decode("utf-8"))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
