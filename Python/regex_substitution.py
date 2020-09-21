# Difficulty : Medium
# Link : https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem
# Language : Python 3

import re
def replace(match):
    if match.group(0)=="&&":
        
        return "and"
    elif match.group(0)=="||":
        return "or"
for i in range(int(input())):
    a=input()
    print(re.sub(r"((?<= )(\&\&)(?= )|(?<= )(\|\|)(?= ))", replace, a))