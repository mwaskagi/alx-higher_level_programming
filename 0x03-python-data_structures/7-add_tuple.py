#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tA = tuple_a + (0, 0)
    tB = tuple_b + (0, 0)
    return tA[0] + tB[0], tA[1] + tB[1]
