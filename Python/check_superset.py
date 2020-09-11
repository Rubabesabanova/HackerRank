# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/py-check-strict-superset/problem
# Language : Python 3

A=set(input().split())
n=int(input())
isSuperset=True
for i in range(n):
    B=set(input().split())
    if not A.issuperset(B):
        isSuperset=False
        break
print(isSuperset)