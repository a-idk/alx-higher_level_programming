#!/usr/bin/python3
def magic_string(lst=[0]):
    lst[0] = lst[0] + 1
    return (str("BestSchool, " * (lst[0] - 1)) + "BestSchool")
