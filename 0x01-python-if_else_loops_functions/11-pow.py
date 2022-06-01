#!/usr/bin/python3
def pow(a, b):
    result = 1
    base = 1
    nb = 0

    if b < 0:
        nb = b
        b = (-1) * b

    for i in range(b):
        result *= a
        base = result * result

    if nb < 0:
        result /= base
    return result
