# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
# Language : Python 3

import numpy
N, M, P=map(int, input().split())
arr1=[]
arr2=[]
for i in range(N):
    arr1.append(list(map(int, input().split())))
for i in range(M):
    arr2.append(list(map(int, input().split())))
print(numpy.concatenate((numpy.array(arr1), numpy.array(arr2)))) 