#!/usr/bin/python3
"""
Title: Only sub class of
Description: function(method) that returns True if the object is an
        instance of a class that inherited (directly or indirectly) from
        the specified class ; otherwise False
@a_idk Scripting
"""


def inherits_from(obj, a_class):
    """ Method that checks or Only sub class of """
    return (isinstance(obj, a_class) and type(obj) != a_class)
