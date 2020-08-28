# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/finding-the-percentage/problem
# Language : Python 3

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    mylist = student_marks[query_name]
    for i in mylist:
        sum += float(i)

    a = sum/len(mylist)

    print('{:.2f}'.format(a))
