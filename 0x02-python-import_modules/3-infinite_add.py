#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    if len(sys.argv) == 1:
        print(0)
    else:
        for arguments in range(1, len(sys.argv)):
            sum = sum + int(sys.argv[arguments])
        print(sum)
