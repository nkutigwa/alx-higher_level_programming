#!/usr/bin/python3
def uppercase(str):
    res = ''
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            res += chr(ord(char) - 32)
        else:
            res += char
    print("{:s}".format(res))
