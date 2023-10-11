#!/usr/bin/python3
# @a_idk scripting

# function that deletes a key in a dictionary


def simple_delete(a_dictionary, key=""):
    a_dictionary.pop(key, None)
    return (a_dictionary)


#    if a_dictionary.get(key) is None:
#        a_dictionary[key] = a_dictionary[key]
#    else:
#        del a_dictionary[key]
#    return (a_dictionary)

#    if a_dictionary.get(key) is not None:
#        del a_dictionary[key]
#    return (a_dictionary)
