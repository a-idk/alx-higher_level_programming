#!/usr/bin/python3
"""
Title: Response header value
Description: A script that takes in a URL, sends a request to the URL and
    displays the value of the variable X-Request-Id in the response header
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
    # content = urllib.parse.urlencode({'email': email_given})
    # content = content.encode('ascii')  # in bytes

    req = requests.get(url_given)
    print(req.headers.get("X-Request-Id"))
    """
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('ascii'))
    except urllib.error.HTTPError as err:
        print(f'Error code: {err.code}')
    """
