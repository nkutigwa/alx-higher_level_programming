#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for i in range(0, 90):
            c += i

        return c
    return sub(a, b)
