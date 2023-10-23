#!/usr/bin/python3

'''
 function that divides element by element 2 lists
@a_idk scripting
'''


def list_division(my_list_1, my_list_2, list_length):
    outcome = []
    for idx in range(list_length):
        try:
            # Acquiring the elements from the lists
            outcome.append(my_list_1[idx] / my_list_2[idx])
        except ZeroDivisionError:
            outcome.append(0)
            print('division by 0')
            continue
        except TypeError:
            outcome.append(0)
            print('wrong type')
            continue
        except IndexError:
            outcome.append(0)
            print('out of range')
            continue
        finally:
            pass
    return outcome
