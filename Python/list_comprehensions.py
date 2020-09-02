# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/list-comprehensions/problem
# Language : Python 3

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    mylists=[[m, p, l] for m in range(x+1) for p in range(y+1) for l in range(z+1) if m+p+l!=n ]
    print(mylists)