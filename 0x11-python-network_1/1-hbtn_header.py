#!/usr/bin/python3
"""
Title: Response header value
Description: A script that takes in a URL, sends a request to the URL and
    displays the value of the X-Request-Id variable found in the header of
    the response
Author: @a_idk
"""
# from urllib import request
import urllib.request
import sys


if __name__ == "__main__":
    arg = sys.argv[1]
    with urllib.request.urlopen(arg) as response:
        print(response.headers["X-Request-Id"])
