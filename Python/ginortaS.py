# Difficulty : Medium
# Link : https://www.hackerrank.com/challenges/ginorts/problem
# Language : Python 3

s=input()
u=[i for i in s if i.isupper()]
l=[i for i in s if i.islower()]
o=[i for i in s if i.isdigit() and int(i)%2==1]
e=[i for i in s if i.isdigit() and int(i)%2==0]
final=list(sorted(l)+sorted(u)+sorted(o)+sorted(e))
print("".join(final))