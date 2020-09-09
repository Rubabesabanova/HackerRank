# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/py-check-subset/problem
# Language : Python 3

for i in range(int(input())):
    a=int(input())
    A=set(map(int, input().split()))
    a=int(input())
    B=set(map(int, input().split()))
    print(A.issubset(B))