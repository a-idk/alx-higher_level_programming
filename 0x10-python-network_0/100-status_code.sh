#!/bin/bash
# script that 1.sends a req to URL passed as arg 2.displays only status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
