#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is "":
        return 0, None
    a = len(sentence)
    b = sentence[:1]
    return a, b
