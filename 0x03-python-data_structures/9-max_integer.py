#!/usr/bin/python3
def max_integer(my_list=[]):
    max_number = my_list[0]
    if not my_list:
        return None
    else:
        for i in my_list:
            if i > max_number:
                max_number = i
    return max_number
