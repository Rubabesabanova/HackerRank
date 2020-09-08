# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/itertools-combinations/problem
# Language : Python 3

from itertools import combinations
whole_input=list(input().split())
main_str=sorted(whole_input[0])
repeated=int(whole_input[1])
start=1
while repeated>=start:
    for i in sorted(list(combinations(main_str, start))):
        print("".join(j for j in i))
    start+=1