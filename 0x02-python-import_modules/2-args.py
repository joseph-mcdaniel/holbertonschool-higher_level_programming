#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0 argument.")

    elif len(argv) == 2:
        print("1 argument:\n1: {:s}".format(argv[1]))

    else:
        print("{:d} arguments:".format(len(argv) - 1))
        for i in argv:
            if argv.index(i) > 0:
                print("{0}: {1}".format(argv.index(i), i))
