#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10

def num(last_digit):
    if last_digit > 5:
        return "and is greater than 5"
    elif last_digit == 0:
        return "and is zero"
    else:
        return "and is less than 6 and not 0"

result = num(last_digit)

print(f"Last digit of {number} is {last_digit} {result}")
