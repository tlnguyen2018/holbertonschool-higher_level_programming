#!/usr/bin/python3
"""
Function create object from json file
"""


import json


def load_from_json_file(filename):
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
