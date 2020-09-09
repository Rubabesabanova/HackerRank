# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
# Language : Python 3

from collections import defaultdict
d = defaultdict(list)
first_input=list(map(int, input().split()))
n=first_input[0]
m=first_input[1]
for i in range(n):d['A'].append(input())
for i in range(m):
    line=[]
    x=input()
    for k in range(len(d['A'])):
        if x==d['A'][k]:
            line.append(str(k+1))
    if not line:
        print(-1)
    else:
        print(" ".join(line))