#!/usr/bin/python3
"""
Title: Search API
Description: A script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
Author: @a_idk
"""
# from urllib import request
# import urllib.error
# import urllib.request
import sys
# import urllib.parse
import requests


if __name__ == "__main__":

    if len(sys.argv) == 1:
        content = ""
    else:
        content = sys.argv[1]

    letter = {"q": content}
    req = requests.post("http://0.0.0.0:5000/search_user", data=letter)
    try:
        if req.json() != {}:
            print(f"[{req.get('id')}] {req.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
