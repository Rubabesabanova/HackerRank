# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/itertools-permutations/problem
# Language : Python 3

from itertools import permutations
whole_input=list(input().split())
main_str=whole_input[0]
repeated=int(whole_input[1])
for i in sorted(list(permutations(main_str, repeated))):
    for k in i:
        print(k, end="")
    print()