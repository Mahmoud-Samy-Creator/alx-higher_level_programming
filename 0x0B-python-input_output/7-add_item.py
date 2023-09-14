#!/usr/bin/python3

""" A python script to add arguments to a list
"""

import json
import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

json_list = []
file = "add_item.json"

json_list = load(file)

for i in range(1, len(sys.argv)):
        json_list.append(sys.argv[i])

save(json_list, file)