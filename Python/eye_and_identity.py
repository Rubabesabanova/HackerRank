# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/np-eye-and-identity/problem
# Language : Python 3

import numpy
numpy.set_printoptions(legacy='1.13')
print(numpy.eye(*list(map(int, input().split()))))
