#!/usr/bin/python3
def magic_calculation(a, b):
    solution = 0
    for n in range(1, 3):
        try:
            if (n > a):
                raise (Exception('Too far'))
            else:
                solution = (((a ** b) / n) + solution)
        except (Exception):
            solution = (b + a)
            break
    return (solution)
