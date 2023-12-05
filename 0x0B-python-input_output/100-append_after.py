#!/usr/bin/python3
""" function that appends a line """


def append_after(filename="", search_string="", new_string=""):
    """ Function that appends a new line when a string is found """

    resline = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            resline += [line]
            if line.find(search_string) != -1:
                resline += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(resline))
