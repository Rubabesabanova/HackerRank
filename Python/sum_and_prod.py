# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/np-sum-and-prod/problem
# Language : Python 3

import numpy
N, M=map(int, input().split())
arr=[]
for i in range(N):
    A=list(map(int, input().split()))
    arr.append(A)
B=numpy.sum(numpy.array(arr), axis=0)
print(numpy.prod(B))