# Difficulty : Medium
# Link : https://www.hackerrank.com/challenges/no-idea/problem
# Language : Python 3

n,m=map(int, input().split())
happiness=0
N=input().split()
A=set(input().split())
B=set(input().split())
for i in N:
    if i in A:
        happiness+=1
    elif i in B:
        happiness-=1
print(happiness)