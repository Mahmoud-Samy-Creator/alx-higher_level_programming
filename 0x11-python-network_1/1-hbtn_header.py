#!/usr/bin/python3
# Send request to url, display value of header

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    url = argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        print(response.info().get("X-Request-Id"))

