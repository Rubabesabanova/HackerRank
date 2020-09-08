# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/py-set-mutations/problem
# Language : Python 3

n=int(input())
A=set(map(int, input().split()))
number_commands=int(input())
for i in range(number_commands):
    command=input().split()
    B=set(map(int, input().split()))
    if command[0]=="intersection_update":
        A.intersection_update(B)
    elif command[0]=="symmetric_difference_update":
        A.symmetric_difference_update(B)
    elif command[0]=="difference_update":
        A.difference_update(B)
    elif command[0]=="update":
        A.update(B)
print(sum(A))