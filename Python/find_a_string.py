# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/find-a-string/problem
# Language : Python 3

def count_substring(string, sub_string):
    start = 0
    end = len(sub_string)
    str = ""
    times = 0
    while end <= len(string):
        str = ""
        for i in range(start, end):
            str += string[i]
        if str == sub_string:
            times += 1
        start += 1
        end += 1
    else:
        return times


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
