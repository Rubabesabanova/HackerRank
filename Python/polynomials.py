# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/np-polynomials/problem
# Language : Python 3

import numpy
print(numpy.polyval(numpy.array(list(map(float, input().split()))), int(input())))