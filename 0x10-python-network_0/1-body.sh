#!/bin/bash
# a Bash script that takes in a URL, sends a GET request to the URL,
# and displays the body of the response (200 only)

curl -sL "$1"
