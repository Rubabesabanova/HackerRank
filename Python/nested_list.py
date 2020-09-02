# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/nested-list/problem
# Language : Python 3

records=scores=names=[]
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    scores.append(score)
    records.append([name, score])

secondlowest=sorted(set(scores))[1]
for i in records:
    if i[1]==secondlowest:
        names.append(i[0])
for i in sorted(names):
    print(i)