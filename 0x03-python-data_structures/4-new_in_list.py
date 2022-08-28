#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """A function that replaces an element in a list"""
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
        
    my_list1 = my_list[:]
    my_list1[idx] = element
    return my_list1
