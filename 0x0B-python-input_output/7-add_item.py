#!/usr/bin/python3
"""
script adds arguments to python list and saves to a file
"""

from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

fname = "add_item.json"

try:
    jsonls = load_from_json_file(fname)
except FileNotFoundError:
    jsonls = []

for arg in argv[1:]:
    jsonls.append(arg)

save_to_json_file(jsonls, fname)
