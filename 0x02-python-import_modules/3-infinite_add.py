#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print(0)
    else:
        n = 1
        sum = 0
        for i in argv:
            sum += int(argv[n])
            n += 1
            if n > (len(argv) - 1):
                break
        print(sum)
