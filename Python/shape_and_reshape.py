# Difficulty : Medium
# Link : https://www.hackerrank.com/challenges/np-shape-reshape/problem
# Language : Python 3

import numpy
print(numpy.reshape(numpy.array(list(map(int, input().split()))), (3,3)))