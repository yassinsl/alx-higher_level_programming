#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        print("{}{}".format(i,j),end='')
        if (i != 9 or j != 9):
            print(", ",end='')