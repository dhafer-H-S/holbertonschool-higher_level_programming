#!/usr/bin/python3
from contextlib import nullcontext
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = number * -1
    digit = number % 10
    rest = 'and is less than 6 and not 0'
    if digit == 0:
        print(f"Last digit of {number * -1} is {digit} and is 0")
    else:
        print(f"Last digit of {number * -1} is {digit * -1} {rest}")

else:
    digit = number % 10
    if digit > 5:
        print(f"Last digit of {number} is {digit} and is greater than 5")
    elif digit > 0 and digit < 6:
        print(f"Last digit of {number} is {digit} {rest}")
    elif digit == 0:
        print(f"Last digit of {number * -1} is {digit} and is 0")
