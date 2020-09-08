# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
# Language : Python 3

def average(array):
    total_sum=sum(set(array))
    return total_sum/len(set(array))
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)