# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/python-string-formatting/problem
# Language : Python 3

def print_formatted(number):
    maxlength=len(str(bin(number)[2:]))
    for i in range(1, number+1):
        x=oct(i)[2:]
        y=hex(i)[2:].upper()
        z=bin(i)[2:]
        print("{} {} {} {}".format(str(i).rjust( maxlength, " "), x.rjust( maxlength, " "), y.rjust( maxlength, " "), z.rjust( maxlength, " ")))

n = 17
print_formatted(n)