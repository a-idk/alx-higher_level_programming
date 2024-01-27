#!/usr/bin/python3
"""
Title: Error code (requests)
Description: A script that takes in a URL and displays the body of the response
    Also gives error code if http encounters error.
Author: @a_idk
"""
# from urllib import request
# import urllib.error
# import urllib.request
import sys
# import urllib.parse
import requests


if __name__ == "__main__":
    url_given = sys.argv[1]
    # email_given = sys.argv[2]
    # encoding the email
    content = requests.get(url_given)

    if content.status_code < 400:
        print(content.text)
    else:
        print(f'Error code: {content.status_code}')
