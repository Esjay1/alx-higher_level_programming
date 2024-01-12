#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        print("{} argument".format((len(sys.argv) - 1)), end='')
    if len(sys.argv) != 2:
        print("{} arguments".format((len(sys.argv) - 1)), end='')
    if len(sys.argv) == 1:
        print(".", end='\n')
    if len(sys.argv) > 1:
        print(":", end='\n')
        i = 1
        while i <= (len(sys.argv) - 1):
            print("{}: {}".format(i, (sys.argv[i])), end="\n")
            i += 1
