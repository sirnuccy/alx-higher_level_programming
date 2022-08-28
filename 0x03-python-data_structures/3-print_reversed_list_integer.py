#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return

    rev = my_list.reverse()
    for i in range(len(rev)):
        print('{}'.format(rev[i]))
