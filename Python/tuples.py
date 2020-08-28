# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/python-tuples/problem
# Language : Python 3

if __name__ == '__main__':
    n = int(input())
    mytuple = []
    integer_list = map(int, input().split())
    for i in integer_list:
        mytuple.append(i)

    print(hash(tuple(mytuple)))
