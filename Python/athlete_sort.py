# Difficulty : Medium
# Link : https://www.hackerrank.com/challenges/python-sort-sort/problem
# Language : Python 3

import math
import os
import random
import re
import sys
from collections import namedtuple


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []
    
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k=int(input())
    
    def K(arr):
        return arr[k]
    arr.sort(key=K)
            
    print("\n".join(" ".join(str(i) for i in j) for j in arr))