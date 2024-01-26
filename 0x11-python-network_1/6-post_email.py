#!/usr/bin/python3
"""
Title: POST an email (requests)
Description: A script that takes in a URL and an email address, sends a POST
    request to the passed URL with the email as a parameter, and finally
    displays the body of the response.
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
    email_given = sys.argv[2]
    # encoding the email
    content = requests.post(url_given, {'email': email_given})

    print(content.text)
    """
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('ascii'))
    except urllib.error.HTTPError as err:
        print(f'Error code: {err.code}')
    """
