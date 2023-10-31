#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
   tens = number % 10
else
   tens = number % -10
if tens > 5:
   print(f"Last digit of {number:d} is {tens:d} and is greater than 5")
elif tens == 0:
   print(f"Last digit of {number:d} is {tens:d} and is 0")
elif tens < 6:
   print(f"Last digit of {number:d} is {tens:d} and is less than 6 and not 0")
