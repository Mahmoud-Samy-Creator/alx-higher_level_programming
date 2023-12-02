#!/bin/bash
# Display all methods that the server will exept
curl -sI "$1" | grep Allow: | cut -d ' ' -f 2