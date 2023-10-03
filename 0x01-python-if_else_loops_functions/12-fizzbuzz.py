#!/usr/bin/python3
# @a_idk scripting

''' function that prints the numbers from 1 to 100
separated by a space.'''


def fizzbuzz():
     for num in range(1, 101):
         # for multiples of both three and five print FizzBuzz
         if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz ", end="")
        # For multiples of three print Fizz
        elif num % 3 == 0:
            print("Fizz ", end="")
        # for multiples of five print Buzz
        elif num % 5 == 0:
            print("Buzz ", end="")
        # skip
        else:
            print("{} ".format(num), end="")
