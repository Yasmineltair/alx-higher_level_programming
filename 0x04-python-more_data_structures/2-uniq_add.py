#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for number in my_list:
        if my_list.count(number) == 1:
            sum += number
    return (sum)
