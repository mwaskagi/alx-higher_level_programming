#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for a, b in a_dictionary.items():
            if b == value:
                del a_dictionary[a]
                break
    return (a_dictionary)
