# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/np-min-and-max/problem
# Language : Python 3

import numpy
N, M =map(int, input().split())
arr=[]
for i in range(N):
    arr.append(list(map(int, input().split())))
A=numpy.min(arr, axis=1)
print(numpy.max(A))