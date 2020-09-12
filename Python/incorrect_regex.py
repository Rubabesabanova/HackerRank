# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/incorrect-regex/problem
# Language : Python 3

import re
for i in range(int(input())):
    line=input()
    try:
        re.compile(line)
        print(True)
    except:
        print(False)