#!/bin/bash
# script that 1.takes URL as arg 2.sends POST req 3.displays the body of response
curl -sXd POST "email=test@gmail.com&subject=I will always be here for PLD" "${1}"
