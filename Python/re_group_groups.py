# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/re-group-groups/problem
# Language : Python 3

import re
m = re.search(r'([a-zA-Z0-9])\1+',input())
print(m.group(1) if m!=None else "-1" )