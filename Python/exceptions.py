# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/exceptions/problem
# Language : Python 3

for i in range(int(input())):
    try:
        line=list(map(int, input().split()))
        print(line[0]//line[1])
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)