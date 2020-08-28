# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/a-very-big-sum/problem
# Language : Python 3


import math
import os
import random
import re
import sys


def aVeryBigSum(ar):
    sum = 0
    for i in range(0, ar_count):
        sum += ar[i]
    return sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
