#!/usr/bin/python3
"""
Add all arg to python list
save to file
list must save in json presentation
"""


import sys
import json


save_file = __import__('7-save_to_json_file').save_to_json_file
load_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    f = load_file(filename)
except:
    f = []
for args in sys.argv[1:]:
    f.append(args)
save_file(f, filename)
