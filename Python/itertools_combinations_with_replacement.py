# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
# Language : Python 3

from itertools import combinations_with_replacement
whole_input=list(input().split())
main_str=sorted(whole_input[0])
repeated=int(whole_input[1])
for i in sorted(list(combinations_with_replacement(main_str, repeated))):
    print("".join(j for j in i))