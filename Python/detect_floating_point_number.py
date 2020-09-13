# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/introduction-to-regex/problem
# Language : Python 3

import re
for i in range(int(input())):
    line=input()
    x = re.match("^([+-])?[0-9]*\.[0-9]+$",line)
    print(bool(x))