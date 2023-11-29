#!/usr/bin/python3
def magic_string(static={"iteration": 0}):
    static["iteration"] += 1
    return str("BestSchool, " * static["iteration"])[:-2]
