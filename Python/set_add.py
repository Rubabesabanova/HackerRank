# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/py-set-add/problem
# Language : Python 3

number_input=int(input())
stamps_set=set()
for i in range(number_input):
    stamps_set.add(input())
print(len(stamps_set))