# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
# Language : Python 3

cube = lambda x: x**3

def fibonacci(n):
    fibonacci=[]
    for i in range(n):
        if i==0 or i==1:
            fibonacci.append(i)
        else: fibonacci.append(fibonacci[-1]+fibonacci[-2])
    return fibonacci
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))