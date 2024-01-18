#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argement = len(sys.argv) - 1
    if argement == 1:
        print ("{} argument:".format(argement))
    elif argement == 0:
        print("{} arguments.".format(argement))
    else:
        print("{} arguments:".format(argement))
    for i in (range(1, argement  + 1)):
        print("{}: {}".format(i, sys.argv[i]))
