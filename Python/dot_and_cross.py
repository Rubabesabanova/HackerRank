# Difficulty : Easy
# Link : hackerrank.com/challenges/np-dot-and-cross/problem
# Language : Python 3

import numpy
N=int(input())
A=[]
B=[]
numpy.set_printoptions(legacy='1.13')
for i in range(N):
    A.append(list(map(int, input().split())))
for i in range(N):
    B.append(list(map(int, input().split())))
print(numpy.dot(A, B))
