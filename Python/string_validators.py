# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/string-validators/problem
# Language : Python 3

if __name__ == '__main__':
    s = input()
    isAlnum = isAlpha = isDigit = isLower = isUpper = False
    for i in s:
        if i.isalnum():
            isAlnum = True
        if i.isalpha():
            isAlpha = True
        if i.isdigit():
            isDigit = True
        if i.islower():
            isLower = True
        if i.isupper():
            isUpper = True

    print(isAlnum)
    print(isAlpha)
    print(isDigit)
    print(isLower)
    print(isUpper)
