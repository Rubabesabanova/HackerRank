# Difficulty : Medium
# Link : https://www.hackerrank.com/challenges/word-order/problem
# Language : Python 3

from collections import Counter
initial=[]
for i in range(int(input())):
    initial.append(input())

print(len(Counter(initial)))
for k in Counter(initial).values():
    print(k, end=" ")