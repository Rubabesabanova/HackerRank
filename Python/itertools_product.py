# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/itertools-product/problem
# Language : Python 3

from itertools import product
A=list(map(int, input().split()))
B=list(map(int, input().split()))
for i in sorted(list(product(A, B))):
    print(i, end=" ")