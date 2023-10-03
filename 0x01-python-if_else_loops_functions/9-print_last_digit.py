#!/usr/bin/python3
# @a_idk scripting

''' function that prints the last digit
of a number.'''


def print_last_digit(number):
    num = abs(number)
    print(num % 10, end="")
    return (num % 10)
