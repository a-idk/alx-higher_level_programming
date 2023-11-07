#!/usr/bin/python3
"""
Title: Log parsing
Description: Write a script that reads stdin line by line and
    computes metrics
@a_idk scripting
"""


from sys import stdin


"""
Defining and initializing the dict status code to store the HTTP s_code
and initializing the total size to 0
"""
s_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '402': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
        }
t_size = count = 0


def printer():
    """
    function that prints the total file size and the count of status
    codes, sorted in ascending order
    """
    print(f'File size: {t_size}')
    for key, value in sorted(s_codes.items()):
        if value > 0:
            print('{:s}: {:d}'.format(key, value))


try:
    for com in stdin:
        div_line = com.split()
        if len(div_line) >= 2:
            s = div_line[-2]
            t_size = t_size + int(div_line[-1])
            if s in s_codes:
                s_codes[s] = s_codes[s] + 1
        count = count + 1
        if count % 10 == 0:
            printer()
    printer()
except KeyboardInterrupt as e:
    printer()
