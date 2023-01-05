#!/usr/bin/python3
for i in range(26, 0, -1):
    if i % 2 == 0:
        z = 96
    else:
        z = 64
    print("{:s}".format(chr(i + z)), end="")
