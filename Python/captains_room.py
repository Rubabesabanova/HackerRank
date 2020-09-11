# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/py-the-captains-room/problem
# Language : Python 3

k=int(input())
rooms=list(map(int, input().split()))
s=sum(set(rooms))
print((s*k-sum(rooms))//(k-1))
