#!/usr/bin/python3
def no_c(my_string):
    without_c = ""
    for c in range(len(my_string)):
        if (my_string[c] != 'c' and my_string[c] != 'C'):
            without_c += my_string[c]
    return (without_c)
