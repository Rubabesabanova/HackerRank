# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
# Language : Python 3

import re
x=re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?:[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])',input())
print("\n".join(x) if x else -1)