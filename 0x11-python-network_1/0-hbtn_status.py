#!/usr/bin/python3
"""
Title: What's my Status?
Description: A script that fetches "https://alx-intranet.hbtn.io/status"
Author: @a_idk
"""
from urllib import request


if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')

    with urllib.request.urlopen(req) as reponse:
        content = response.read()
        # formating the print as requested
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
