#!/usr/bin/python3
"""
Function that adds arguments
to a python list saved in file
"""

import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = 'add_item.json'
if os.path.exists(filename):
    """
    if there call it else create new
    """
    the_list = load_from_json_file(filename)
else:
    with open(filename, mode='w') as f:
        the_list = []
        save_to_json_file([], filename)

for ar in range(1, len(sys.argv)):
    the_list.append(sys.argv[ar])
    save_to_json_file(the_list, filename)
