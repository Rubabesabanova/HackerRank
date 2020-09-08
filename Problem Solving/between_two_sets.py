# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/between-two-sets/problem
# Language : Python 3

import math
import os
import random
import re
import sys


def getTotalX(a, b):
    first_list=[]
    final=[]
    max_value=min(set(b))
    min_value=min(set(a))
    for i in range(min_value, max_value+1):
        for k in a:
            if i%k==0:
                acceptable=True
            else:
                acceptable=False
                break
        if acceptable:
            first_list.append(i)
    for index in first_list:
        for number in b:
            if number%index==0:
                acceptable=True
            else:
                acceptable=False
                break
        if acceptable:
            final.append(i)
    return len(final)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()