# Difficulty : Medium
# Link : https://www.hackerrank.com/challenges/compress-the-string/problem
# Language : Python 3

from itertools import groupby
string=input()
for i, x in groupby(string):    
    print(tuple([len(list(x)), int(i)]), end=" ")