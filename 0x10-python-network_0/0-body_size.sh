#!/bin/bash
# script that 1.takes in a URL 2.sends a request to that URL, 3. displays the size of the body of the response
curl -s "${1}" | wc -c
