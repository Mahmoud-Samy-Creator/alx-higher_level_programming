#!/bin/bash
# Send GET, Display body, Send a header
curl -sX GET -H "X-School-User-Id: 98" "$1"
