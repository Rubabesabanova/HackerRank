# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/any-or-all/problem
# Language : Python 3

n=int(input())
line=list(map(int, input().split()))
print(all([0 if i<0 else 1 for i in line]) and any([1 if list(str(i))==list(str(i))[::-1]else 0 for i in line]))