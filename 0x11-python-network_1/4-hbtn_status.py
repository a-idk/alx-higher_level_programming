#!/usr/bin/python3
"""
Title: What's my status
Description: A script that fetches https://alx-intranet.hbtn.io/status
Author: @a_idk
"""
# from urllib import request
# import urllib.error
# import urllib.request
# import sys
# import urllib.parse
import requests


if __name__ == "__main__":
    url_given = 'https://alx-intranet.hbtn.io/status'
    # email_given = sys.argv[2]
    # encoding the email
    # content = urllib.parse.urlencode({'email': email_given})
    # content = content.encode('ascii')  # in bytes

    req = requests.get(url_given)
    # print format given
    print('Body response:')
    print('\t- type: {}'.format(type(req.text)))
    print('\t- content: {}'.format(req.text))
    """
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('ascii'))
    except urllib.error.HTTPError as err:
        print(f'Error code: {err.code}')
    """
