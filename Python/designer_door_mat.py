# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/designer-door-mat/problem
# Language : Python 3

n=input().split()
setir=int(n[0])
sutun=int(n[1])
welcome="WELCOME"
design=".|."
for i in range(setir):
    line=""
    design=".|."
    if i<setir//2:
        design=design*(2*i+1)
        line=design.center(sutun, "-")
    if i==setir//2:
        line=welcome.center(sutun, "-")
    elif i>setir//2:
        design=design*(2*(setir-i)-1)
        line=design.center(sutun, "-")
    print(line)