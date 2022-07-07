#!/usr/bin/python3
""""Module to define a rectangle class"""


from sys import argv

if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)

nqueens = argv[1]

if not isinstance(nqueens, int):
    print('N must be a number')
    exit(1)

if nqueens <= 4:
    print('N must be at least 4')
    exit(1)
