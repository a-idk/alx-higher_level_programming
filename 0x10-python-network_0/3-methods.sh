#!/bin/bash
# script that 1.takes in a URL 2.displays all HTTP methods the server will accept
curl -sI "${1}" | grep "^Allow: .*" | cut -d " " -f2-
