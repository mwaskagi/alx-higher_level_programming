#!/usr/bin/python3
def uppercase(str):
    i = 0
    while i < len(str):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            x = chr(ord(str[i]) - 32)
        else:
            x = str[i]
        print("{:s}".format(x), end="")
        i += 1
    print()
