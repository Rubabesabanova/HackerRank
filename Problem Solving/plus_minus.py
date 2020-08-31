# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/plus-minus/problem
# Language : Python 3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    positive=negative=zero=0
    for i in arr:
        if i<0:
            negative+=1
        elif i>0:
            positive+=1
        else:
            zero+=1
    print('{:.4f}'.format(positive/n))
    print('{:.4f}'.format(negative/n))
    print('{:.4f}'.format(zero/n))
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
