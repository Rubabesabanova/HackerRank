# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/collections-counter/problem
# Language : Python 3

from collections import Counter
number_shoes=int(input())
size_shoes=Counter(list(map(int, input().split())))
number_customers=int(input())
money=0
for i in range(number_customers):
    order=list(map(int, input().split()))
    for i in size_shoes.keys(): 
        if order[0]==i and size_shoes[i]>0:
            size_shoes[i]-=1
            money+=order[1]
print(money)