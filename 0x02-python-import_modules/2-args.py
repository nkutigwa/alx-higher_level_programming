#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_args = len(sys.argv)
    if len_args == 1:
        print("{} arguments.".format(len_args - 1))
    elif len_args == 2:
        print("{} argument:".format(len_args - 1))
    else:
        print("{} arguments:".format(len_args - 1))
    for i in range(1, len_args):
        print("{}: {}".format(i, sys.argv[i]))
