#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    while True:
        try:
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
        except IndexError:
            break
        if count >= x:
            break
        i += 1
    print()
    return count
