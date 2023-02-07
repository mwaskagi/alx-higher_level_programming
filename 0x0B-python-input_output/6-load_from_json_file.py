#!/usr/bin/python3
"""
Function that creates oject
from json file
"""
import json


def load_from_json_file(filename):
    """
    load file using json
    """
    with open(filename, mode='r') as f:
        return json.load(f)
