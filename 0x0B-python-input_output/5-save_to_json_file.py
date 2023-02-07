#!/usr/bin/python3
"""
function that writes an object
to a text file with json
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writing to file
    """
    with open(filename, mode='w') as f:
        f.write(json.dumps(my_obj))
