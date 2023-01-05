#!/usr/bin/python3
for i in range(0, 26):
    if i != 4 and i != 16:
        print("{:s}".format(chr(ord('a') + i)), end="")
