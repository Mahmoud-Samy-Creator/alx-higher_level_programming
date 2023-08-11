#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("{} arguments.".format(len(argv) - 1))
    else:
        print("{} arguments:".format(len(argv) - 1))
    for arguments in range(1, len(argv) + 1):
        print("{}: {}".format(arguments, argv[arguments]))
