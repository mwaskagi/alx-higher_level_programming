#!/usr/bin/python3

def write_file(filename="", text=""):
    """
     Function writes a string to a file
     Return the number of charcters
    """
    with open(filename, 'w+') as f:
        return f.write(text)
