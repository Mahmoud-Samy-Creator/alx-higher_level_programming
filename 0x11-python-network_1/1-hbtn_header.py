#!/usr/bin/python3
# Send request to url, display value of header

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    url = argv[1]

    with urllib.request.urlopen(url) as response:
        print(response.info().get("X-Request-Id"))
