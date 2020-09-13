# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/most-commons/problem
# Language : Python 3

import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = sorted(input())
    x=Counter(s).most_common(3)
    for k in x:
        print(k[0], k[1])