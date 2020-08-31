# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/30-operators/problem
# Language : Python 3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    meal_cost +=meal_cost*(tip_percent+tax_percent)/100
    print(round(meal_cost))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
