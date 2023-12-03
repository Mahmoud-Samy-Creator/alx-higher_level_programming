#!/usr/bin/python3
"""
A Python script that takes in a letter
and sends a POST request to
http://0.0.0.0:5000/search_user with the letter
as a parameter.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = "http://0.0.0.0:5000/search_user"

    if len(argv) == 1:
        data = {"q": ""}
    else:
        data = {"q": argv[1]}

    req = requests.post(url, data)

    if req.headers.get("content-type") != "application/json":
        print("Not a valid JSON")

    elif req.json == "":
        print("No result")

    else:
        print("[{}] {}".format(req.json()["id"], req.json()["name"]))
