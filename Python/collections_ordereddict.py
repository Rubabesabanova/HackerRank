# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
# Language : Python 3

from collections import OrderedDict
ordered_dictionary = OrderedDict()
for i in range(int(input())):
    order=input().split()
    indict=False
    for k, y in ordered_dictionary.items():
        if k==" ".join(order[:-1]):
            indict=True
            y+=int(order[-1])
            ordered_dictionary[" ".join(order[:-1])]=y
            break
    if not indict:
        ordered_dictionary[" ".join(order[:-1])]=int(order[-1])
for k, y in ordered_dictionary.items():
    print(k, y)