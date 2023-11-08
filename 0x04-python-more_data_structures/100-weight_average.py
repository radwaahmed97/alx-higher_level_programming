#!/usr/bin/python3
def weight_average(my_list=[]):
    tot_weight = 0
    avg = 0
    tot_score = 0
    if (len(my_list) <= 0):
        return (0)
    for i in my_list:
        score, weight = i
        tot_weight += weight
        tot_score += score * weight
    return (tot_score / tot_weight)
