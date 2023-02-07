#!/usr/bin/python3
"""
Funtion append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    search and update file
    """
    r = []
    with open(filename, mode="r") as f:
        r = f.readlines()
        idx = 0

        while idx < len(r):
            if search_string in r[idx]:
                r[idx:idx + 1] = [r[idx], new_string]
                idx += 1
            idx += 1

    with open(filename, "w") as f2:
        f2.writelines(r)
