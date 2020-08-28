# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/compare-the-triplets/problem
# Language : Python 3

import math
import os
import random
import re
import sys


def compareTriplets(a, b):
    alicepoint = 0
    bobpoint = 0
    final = []
    for i in range(0, 3):
        if a[i] > b[i]:
            alicepoint += 1

        elif a[i] < b[i]:
            bobpoint += 1
    final.append(alicepoint)
    final.append(bobpoint)
    return final


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
