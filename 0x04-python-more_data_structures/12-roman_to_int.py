#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    total = 0
    for r in reversed(roman_string):
        num = roman_d[r]
        total += num if total < num * 5 else -num
    return total
