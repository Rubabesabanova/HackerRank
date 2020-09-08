# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/symmetric-difference/problem
# Language : Python 3

number_n=int(input())
n_list=set(map(int, input().split()))
number_m=int(input())
m_list=set(map(int, input().split()))

for i in sorted(n_list.symmetric_difference(m_list)):
    print(i)