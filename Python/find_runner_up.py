# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Language : Python 3

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr=list(sorted(set(arr)))
    print(arr[-2])