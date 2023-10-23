#!/usr/bin/python3
# import sys

'''
function that executes a function safely
@a_idk scripting
'''


def safe_function(fct, *args):
    import sys

    try:
        return (fct(*args))
    except Exception as exception:
        print("Exception: {}".format(exception), file=sys.stderr)
        return None
