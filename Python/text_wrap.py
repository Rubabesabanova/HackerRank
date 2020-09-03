# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/text-wrap/problem
# Language : Python 3

import textwrap
def wrap(string, max_width):
    wholestring=""
    for i in range(len(string)):
        if i<=len(string)//max_width:
            wholestring+=string[slice(max_width*i,max_width*(i+1))]+"\n"
        elif i==len(string)//max_width+1:
            wholestring+=string[slice(max_width*i, len(string))]+"\n"
            i=len(string)
    return wholestring
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)