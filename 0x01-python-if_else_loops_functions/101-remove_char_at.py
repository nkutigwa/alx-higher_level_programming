#!/usr/bin/python3
def remove_char_at(str, n):
    s1 = ""
    for i in range(len(str)):
        if i != n:
            s1 = s1 + str[i]
    return (s1)
