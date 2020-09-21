# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
# Language : Python 3

import numpy
whole=[]
b=list(map(int, input().split()))
n=b[0]
m=b[1]
for i in range(n):
    x=list(map(int, input().split()))
    whole.append(x)
print(numpy.array(whole).transpose())
print(numpy.array(whole).flatten())