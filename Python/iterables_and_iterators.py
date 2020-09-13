# Difficulty : Medium
# Link : https://www.hackerrank.com/challenges/iterables-and-iterators/problem
# Language : Python 3

from itertools import combinations
N=int(input())
all_combination=list(combinations(input().split(), int(input())))
number_all=len(all_combination)
count=0
for i in all_combination:
    if "a" in i:
        count+=1
print('{:.3f}'.format(count/number_all))