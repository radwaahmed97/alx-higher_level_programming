#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    file = dir(hidden_4)
    long = len(file)
    for i in range(0, long):
        if file[i][0:2] != "__":
            print(file[i])
