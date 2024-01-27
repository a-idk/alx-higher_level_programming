#!/usr/bin/python3
"""
Title: My Github
Description: A script that takes your GitHub credentials (username and
    password) and uses the GitHub API to display your id
Author: @a_idk
"""
# from urllib import request
# import urllib.error
# import urllib.request
import sys
# import urllib.parse
import requests


if __name__ == "__main__":

    git_addr = "https://api.github.com/user"
    # username = sys.rgv[1], passwd = sys.argv[2]

    req = requests.get(git_addr, auth=(sys.argv[1], sys.argv[2]))
    print(req.json().get('id'))
