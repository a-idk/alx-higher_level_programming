#!/bin/bash
# script that 1.makes a req to 0.0.0.0:5000/catch_me causes server to respond You got me!
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:HolbertonSchool"
