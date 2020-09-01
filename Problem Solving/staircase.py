# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/staircase/problem
# Language : Python 3
def staircase(n):
    for i in range(n):
        pattern=""
        for k in range(n):
            if k>=n-(i+1):
                pattern+="#"
            else:
                pattern +=" "
        print(pattern)
if __name__ == '__main__':
    n = int(input())

    staircase(n)
