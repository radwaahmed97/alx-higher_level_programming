#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    else:
        target = my_list[0]
        for i in range(1, len(my_list)):
            if target < my_list[i]:
                target = my_list[i]
            else:
                continue
        return target
