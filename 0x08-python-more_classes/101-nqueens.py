#!/usr/bin/python3
"""
nqueens backtracking program to print coordinates of n-queens
on an NxN grid that they are all in non-attacking post
"""


from sys import argv

if __name__ == "__main__":
    post = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # initializing answer list
    for i in range(n):
        post.append([i, None])

    def already_exists(y):
        """check that a queen is not in that y value"""
        for x in range(n):
            if y == post[x][1]:
                return True
        return False

    def reject(x, y):
        """checks solution"""
        if (already_exists(y)):
            return False
        i = 0
        while(i < x):
            if abs(post[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_a(x):
        """clears the answers from point of failure"""
        for i in range(x, n):
            post[i][1] = None

    def nqueens(x):
        """recursive backtracking function to determine solution"""
        for y in range(n):
            clear_a(x)
            if reject(x, y):
                post[x][1] = y
                if (x == n - 1): # accepting solution
                    print(post)
                else:
                    nqueens(x + 1) # moves to next x value to cont.

    # starting recursive process at x = 0
    nqueens(0)
