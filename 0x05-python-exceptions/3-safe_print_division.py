#!/usr/bin/python3

'''
function that divides 2 integers and prints the result
@a_idk scripting
'''


def safe_print_division(a, b):
    division = None
    try:
        division = a / b
    except ZeroDivisionError:
        return None
#    except Exception:
#        print("Inside result: {}".format(Exception))
#        return None
    finally:
        if division is not None:
            div_output = "Inside result: {:.1f}".format(division)
        else:
            div_output = "Inside result: None"
        print(div_output)
        return division
