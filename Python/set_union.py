# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/py-set-union/problem
# Language : Python 3

n=int(input())
n_set=set(input().split())
m=int(input())
m_set=set(input().split())
print(len(n_set.union(m_set)))