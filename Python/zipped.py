# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/zipped/problem
# Language : Python 3

first_input=list(map(int, input().split()))
n=first_input[0]
m=first_input[1]
subjects=[]
for i in range(m):
    subjects.append(input().split())
for k in list(zip(*subjects)):
    total_sum=0
    for point in k:total_sum+=float(point)
    print(float(total_sum/len(k)))