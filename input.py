# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/input/problem
# Language : Python 3

first_input=list(map(int,input().split()))
x=first_input[0]
y=first_input[1]
formula=input()
print(y==eval(formula))