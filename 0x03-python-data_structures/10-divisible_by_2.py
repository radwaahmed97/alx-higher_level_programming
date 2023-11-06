#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for n in my_list:
        if n % 2 == 0:
            new_list[new_list.index(n)] = 1
        else:
            new_list[new_list.index(n)] = 0
    return (new_list)
