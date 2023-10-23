#!/usr/bin/python3

'''
function that divides 2 integers and prints the result
@a_idk scripting
'''


def list_division(my_list_1, my_list_2, list_length):
    outcome = []
    for idx in range(list_length):
        try:
            # Acquiring the elements from the lists
            x = my_list_1[idx] if idx < len(my_list_1) else 0
            y = my_list_2[idx] if idx < len(my_list_2) else 0
            # type check
            if not isinstance(x, (int, float)) or \
               not isinstance(y, (int, float)):
                raise TypeError("wrong type")
            if y == 0:  # division by zero check
                raise ZeroDivisionError("division by 0")
            # appending subsequent outcomes/results
            division = x / y
            if division.is_integer():
                outcome.append(float(division))
            else:
                outcome.append(division)
        # handling and printing exceptions
        except TypeError as exception:
            print(exception)
            outcome.append(0)
        except ZeroDivisionError as exception:
            print(exception)
            outcome.append(0)
#        except IndexError:
#            print("out of range")
#            outcome.append(0.0)
    if list_length > max(len(my_list_1), len(my_list_2)):
        outcome.append(0.0)
    if 0.0 in outcome:
        print("out of range")
#        outcome.append(0.0)
    return outcome
