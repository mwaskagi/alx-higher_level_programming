#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    i = 0
    lengthh = len(str)
    if n < 0 or lengthh < n:
        return str
    else:
        while lengthh > i:
            if n == i:
                i += 1
                continue
            s += str[i]
            i += 1
        return s
