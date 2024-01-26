#!/usr/bin/python3
"""
Title: What's my Status?
Description: A script that fetches "https://alx-intranet.hbtn.io/status"
Author: @a_idk
"""
# from urllib import request
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')

    with urllib.request.urlopen(req) as response:
        cont = response.read()
        # formating the print as requested
        print("Body response:")
        print("\t- type: {}".format(type(cont)))
        print("\t- content: {}".format(cont))
        print("\t- utf8 content: {}".format(cont.decode("utf-8")))
