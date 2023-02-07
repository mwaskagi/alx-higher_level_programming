#!/usr/bin/python3
"""
Function that returns an object represented
by Json string
"""
import json


def from_json_string(my_str):
    """
      Decoding Json
    """
    return json.loads(my_str)
