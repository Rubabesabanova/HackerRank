# Difficulty : Medium
# Link : https://www.hackerrank.com/challenges/find-angle/problem
# Language : Python 3

from math import *
a=int(input())
b=int(input())
x=round(degrees(atan(a/b)))
print(str(x)+'°')