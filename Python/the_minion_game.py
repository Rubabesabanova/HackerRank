# Difficulty : Medium
# Link : https://www.hackerrank.com/challenges/the-minion-game/problem
# Language : Python 3

from itertools import permutations
def minion_game(string):
    stuart=kevin=0
    vowels=["A", "E", "I", "O", "U"]
    for i in range(len(string)):
        if string[i] in vowels:
            kevin+=len(string)-i
        else:
            stuart+=len(string)-i
    if kevin>stuart:
        print(f"Kevin {kevin}")
    elif kevin<stuart:
        print(f"Stuart {stuart}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)