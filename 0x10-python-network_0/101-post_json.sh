#!/bin/bash
# script that 1.sends JSON POST req to URL passed as 1st arg 2.displays body of response
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
