# Difficulty : Medium
# Link : https://www.hackerrank.com/challenges/piling-up/problem
# Language : Python 3

from collections import deque
for i in range(int(input())):
    N=int(input())
    length=deque((map(int, input().split())))
    condition="Yes"
    while len(length)>1:
        maxx=max(length[0], length[-1])
        if maxx==length[0]:
            x=length.popleft()
            if x<length[0] or x<length[-1]:
                condition="No"
                break
            else:
                length.popleft()
                length.pop()
        elif maxx==length[-1]:
            x=length.pop()
            if x<length[0] or x<length[-1]:
                condition="No"
                break
            else:
                length.popleft()
                if len(length):
                    length.pop()
        else:
            length.popleft()
            length.pop()
            if maxx<length[0] or maxx<length[-1]:
                condition="No"
                break
            else:
                length.popleft()
                length.pop()
    print(condition)
