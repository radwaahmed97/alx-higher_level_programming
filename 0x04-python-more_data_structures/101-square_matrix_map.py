#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map((lambda segment: list(map((lambda i: i * i), segment))), matrix))
