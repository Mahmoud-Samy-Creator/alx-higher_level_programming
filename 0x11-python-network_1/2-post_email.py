#!/usr/bin/python3
"""
Takes in url, email, sends a POST request with url
"""

if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv

    # Get url & email
    url = argv[1]
    email = argv[2]

    # Define data to be sent
    values = {"email": email}

    # Encoding and parsing
    data = parse.urlencode(values)

    # decoded
    data = data.encode()

    # POST request
    req = request.Request(url, data)

    # Reciving response
    with request.urlopen(req) as response:
        result = response.read()
    print(result.decode("utf-8"))
