# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
# Language : Python 3

import numpy
A=numpy.array(list(map(float, input().split())))
numpy.set_printoptions(legacy='1.13')
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))