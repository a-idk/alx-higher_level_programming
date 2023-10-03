#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lst_dig = abs(number) % 10
if lst_dig > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lst_dig)
elif lst_dig == 0:
    print("Last digit of {} is {} and is 0".format(number, lst_dig)
else:
    print(f"Last digit of {number} is {lst_dig} and is less than 6 and not 0")
