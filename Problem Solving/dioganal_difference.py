# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/diagonal-difference/problem
# Language : Python 3

import math
import os
import random
import re
import sys


def diagonalDifference(n, arr):
    # Write your code here
    sum01=sum02=0
    for i in range(n):
        sum01+= arr[i][i]
        sum02+= arr[i][n-1-i]
    return abs(sum01-sum02)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
