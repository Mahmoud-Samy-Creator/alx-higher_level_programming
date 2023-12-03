#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request
to the URL and displays the body of the response.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]

    status = requests.get(url)

    code = status.status_code

    if code >= 400:
        print(f"Error code: {code}")
    else:
        print(status.text)
