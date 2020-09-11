# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/py-collections-deque/problem
# Language : Python 3

from collections import deque
d = deque()
for i in range(int(input())):
    line=input().split()
    if line[0]=="append":
        d.append(line[1])
    elif line[0]=="appendleft":
        d.appendleft(line[1])
    elif line[0]=="pop":
        d.pop()
    elif line[0]=="popleft":
        d.popleft()
print(" ".join(d))