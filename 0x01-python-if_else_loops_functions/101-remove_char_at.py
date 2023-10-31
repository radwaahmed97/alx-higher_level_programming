#!/usr/bin/python3
def remove_char_at(str, n):
    v = ""
    for i, c in enumerate(str):
        if i is n:
            v += ''
        else:
            v += c
    return v
