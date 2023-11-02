#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0 arguments.")
    if len(argv) == 2:
        print(f"1 argument:")
        print(f"1: {argv[1]}")
    elif len(argv) > 2:
        print(f"{len(argv)-1} arguments:")
        i = 1
        for n in argv:
            print(f"{i}: {argv[i]}")
            i += 1
            if i > (len(argv) - 1):
                break
