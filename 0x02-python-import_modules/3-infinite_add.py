#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    for i in argv:
        if argv.index(i) > 0:
            sum += int(i)
    print('{:d}'.format(sum))
