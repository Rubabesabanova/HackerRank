# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/30-class-vs-instance/problem
# Language : Python 3

class Person:
    def __init__(self,initialAge):
        self.age=initialAge
        if initialAge<0:
            self.age=0
            print("Age is not valid, setting age to 0.")
    def amIOld(self):
        if self.age<13:
            print("You are young.")
        elif self.age>=13 and self.age<18:
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        self.age +=1
t = int(input())