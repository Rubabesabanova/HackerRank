# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/re-start-re-end/problem
# Language : Python 3

import re
k=input()
m=input()
start=0
end=len(m)
if re.search(m, k)==None:
    print("(-1, -1)")
else:
    while end<len(k)+1:
        line=""
        for i in range(start, end):
            line+=k[i]
        x=re.match(m, line)
        if x!=None:
            print("({}, {})".format(start, end-1))
        start+=1
        end+=1