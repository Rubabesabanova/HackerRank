# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/python-mutations/problem
# Language : Python 3

def mutate_string(string, position, character):
    mylist = list(string)
    mylist[position] = character
    mystring = "".join(mylist)
    return mystring


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
