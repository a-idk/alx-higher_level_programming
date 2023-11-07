#!/usr/bin/python3
"""
Title: Load, add, save
Description: Write a script that adds all arguments to a Python list,
    and then save them to a file
"""
import json
import sys
from sys import argv
import os.path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


""" initializing variables """
file_name = "add_item.json"
json_dat = []

""" Loading """
if os.path.exists(file_name):
    json_dat = load_from_json_file(file_name)

""" adding/appending """
for i in argv[1:]:
    json_dat.append(i)

""" saving """
save_to_json_file(json_dat, file_name)
