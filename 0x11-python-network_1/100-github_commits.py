#!/usr/bin/python3
"""
Title: My Github Commits
Description: A script that list 10 commits (from the most recent to oldest)
    of the repository
Author: @a_idk
"""
# from urllib import request
# import urllib.error
# import urllib.request
import sys
# import urllib.parse
import requests


if __name__ == "__main__":

    repository = sys.argv[1]
    owner = sys.argv[2]
    git_addr = f"https://api.github.com/repos/{owner}/{repository}/commits"

    req = requests.get(git_addr)
    count = 0
    for i in req.json():
        key = i.get('sha')
        auth = i.get('commit').get('author').get('name')
        print(f'{key}: {auth}')
        if count > 8:
            break
        count = count + 1
