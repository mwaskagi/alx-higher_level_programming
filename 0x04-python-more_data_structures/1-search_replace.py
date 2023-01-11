#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    a = 1
    for i in my_list:
        if a == search:
            new_list.insert(search, replace)
        else:
            new_list.append(i)
        a += 1
    return new_list
