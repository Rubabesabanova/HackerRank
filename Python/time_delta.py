# Difficulty : Medium
# Link : https://www.hackerrank.com/challenges/python-time-delta/problem
# Language : Python 3


import math
import os
import random
import re
import sys
import calendar
from datetime import datetime

def time_delta(t1, t2):
    t_1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    t_2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    return str(abs(int((t_1-t_2).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()