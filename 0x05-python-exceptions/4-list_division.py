#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    idx1, idx2, count = 0, 0, 0
    new = [x for x in range(list_length)]
    while count < list_length:
        try:
            if type(my_list_1[idx1]) is int or type(my_list_1[idx1]) is float:
                if type(my_list_1[idx2]) is int or type(my_list_1[idx2]) is float:
                    new[count] = my_list_1[idx1] / my_list_2[idx2]
                    idx1 += 1
                    idx2 += 1
                else:
                    idx2 += 1
            else:
                idx1 += 1
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            count += 1
            return new
