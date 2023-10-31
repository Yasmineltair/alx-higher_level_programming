#!/usr/bin/python3
for k in range(0, 10):
    for n in range(1, 10):
        if k >= n:
            continue
        elif k == 8 and n == 9:
            print("{}{}".format(k, n))
        elif k < n:
            print("{}{}, ".format(k, n), end="")
