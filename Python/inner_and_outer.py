# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/np-inner-and-outer/problem
# Language : Python 3

import numpy
A=numpy.array(list(map(int, input().split())))
B=numpy.array(list(map(int, input().split())))

print(numpy.inner(A, B))
print(numpy.outer(A, B))