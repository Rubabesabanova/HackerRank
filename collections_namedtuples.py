# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
# Language : Python 3

from collections import namedtuple
number_students=int(input())
Student = namedtuple("Students",",".join(input().split()))
total_sum=0
for i in range(number_students): 
    total_sum+=int(Student(*input().split()).MARKS)
print(total_sum/number_students)