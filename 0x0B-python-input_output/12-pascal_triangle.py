#!/usr/bin/python3
"""pascal_triangle function"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s
                            triangle of
    """
    if n <= 0:
        return []

    triangless = [[1]]
    while len(triangless) != n:
        tri = triangless[-1]
        tempo = [1]
        for i in range(len(tri) - 1):
            tempo.append(tri[i] + tri[i + 1])
        tempo.append(1)
        triangless.append(tempo)
    return triangless
