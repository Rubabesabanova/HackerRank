# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
# Language : Python 3

import numpy
N, M =map(int, input().split())
arr=[]
numpy.set_printoptions(legacy='1.13')
for i in range(N):
    arr.append(list(map(int, input().split())))
print(numpy.mean(numpy.array(arr), axis=1))
print(numpy.var(numpy.array(arr), axis=0))
print(numpy.std(numpy.array(arr)))