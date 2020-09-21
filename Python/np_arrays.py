# Difficulty : Medium
# Link : https://www.hackerrank.com/challenges/np-arrays/problem
# Language : Python 3

import numpy

def arrays(arr):
    a= numpy.array(arr, float)
    return a[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
