#!/usr/bin/python3
# @a_idk scripting

# function that returns a key with the biggest integer value


def best_score(a_dictionary):
    # If no score found
    if not a_dictionary:
        return (None)
    return (max(a_dictionary, key=a_dictionary.get))
