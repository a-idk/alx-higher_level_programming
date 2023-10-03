#!/usr/bin/python3

# printing all possible combination of 2-digits
# from 0 to 10

for f_dig in range(0, 10):
    for s_dig in range(f_dig + 1, 10):
        if f_dig == 8 and s_dig == 9:
            print("{}{}".format(f_dig, s_dig))
        else:
            print("{}{}".format(f_dig, s_dig), end=", ")
