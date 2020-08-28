# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/simple-array-sum/problem
# Language : Python 3

import os
import sys

def simpleArraySum(ar):

    sum = 0
    for i in range(0, ar_count):
      sum = ar[i]+ sum
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
