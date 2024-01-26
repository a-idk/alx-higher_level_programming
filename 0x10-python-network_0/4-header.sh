#!/bin/bash
# script that 1.takes URL as arg 2.sends GET req 3.displays the body of response
curl -sH "${1}" "X-School-User-Id: 98"
