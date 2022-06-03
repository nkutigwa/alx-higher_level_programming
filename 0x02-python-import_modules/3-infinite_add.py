#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_args = len(sys.argv)
    total = 0
    if len_args == 1:
        total = 0
    else:
        for i in range(1, len_args):
            total += int(sys.argv[i])
    print("{}".format(total))
