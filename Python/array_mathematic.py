# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/np-array-mathematics/problem
# Language : Python 3

import numpy
N, M=map(int, input().split())
A=[]
B=[]
for i in range(N):
    A.append(list(map(int, input().split())))
for i in range(N):
    B.append(list(map(int, input().split())))
A=numpy.array(A)
B=numpy.array(B)
print(numpy.add(A, B))
print(numpy.subtract(A, B))
print(numpy.multiply(A, B))
print(A//B)
print(numpy.mod(A, B))
print(numpy.power(A, B))