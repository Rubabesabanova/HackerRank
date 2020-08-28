# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/swap-case/problem
# Language : Python 3

def swap_case(s):
    str = ""
    for i in s:
        if i == i.lower():
            str += i.upper()
        else:
            str += i.lower()
    return str


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
