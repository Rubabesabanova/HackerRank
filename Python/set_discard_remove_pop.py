# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
# Language : Python 3

n = int(input())
s = set(map(int, input().split()))
number_commands=int(input())
for i in range(number_commands):
    i=input().split()
    if i[0]=="pop":
        s.pop()
    elif i[0]=="remove":
        s.remove(int(i[1]))
    elif i[0]=="discard":
        s.discard(int(i[1]))
print(sum(s))