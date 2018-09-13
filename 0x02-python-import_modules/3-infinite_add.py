#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    for idx in range(1, len(sys.argv)):
        sum += int(sys.argv[idx])
    print("{:d}".format(sum))
