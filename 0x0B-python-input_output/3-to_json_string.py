#!/usr/bin/python3
"""
function that returns Json representation
of object
"""

import json


def to_json_string(my_obj):
    """
    convert object into a json string
    """
    return json.dumps(my_obj)
