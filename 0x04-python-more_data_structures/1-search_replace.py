#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return None
    my_list1 = my_list.copy()
    for i in range(len(my_list1)):
        if my_list1[i] == search:
            my_list1[i] = replace
    return my_list1
