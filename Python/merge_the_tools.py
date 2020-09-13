# Difficulty : Medium
# Link : https://www.hackerrank.com/challenges/merge-the-tools/problem
# Language : Python 3

def merge_the_tools(string, k):
    end=k
    start=0
    while end<=len(string):
        line=[]
        for i in range(start, end):
            if string[i] not in line:
                line.append(string[i])
        print("".join(line))
        end+=k
        start+=k
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)