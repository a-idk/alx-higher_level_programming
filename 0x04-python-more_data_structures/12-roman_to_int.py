#!/usr/bin/python3
# @a_idk scripting

# function that converts a Roman numeral to an integer


def roman_to_int(roman_string):
    # If the roman_string is not a string or None
    if not roman_string:
        return (0)
    if not isinstance(roman_string, str):
        return (0)

    # defining the roman numerals
    r_num = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    # initializing variables
    r2int = 0
    prev_num = 0
    # converting the roman numerals
    for idx in reversed(roman_string):
        num = r_num.get(idx, 0)
        if num < prev_num:
            r2int = r2int - num
        else:
            r2int = r2int + num
        prev_num = num
    return (r2int)
