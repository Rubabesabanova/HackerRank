# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/python-lists/problem
# Language : Python 3

if __name__ == '__main__':
    N = int(input())
    commands = []
    realList = []
    for i in range(N):
        command = input()
        commands.append(command)
    for i in commands:
        mycommand = i.split()
        if mycommand[0] == "insert":
            realList.insert(int(mycommand[1]), int(mycommand[2]))
        elif mycommand[0] == 'print':
            print(realList)
        elif mycommand[0] == "remove":
            realList.remove(int(mycommand[1]))
        elif mycommand[0] == "append":
            realList.append(int(mycommand[1]))
        elif mycommand[0] == "sort":
            realList.sort()
        elif mycommand[0] == "pop":
            realList.pop()
        elif mycommand[0] == "reverse":
            realList.reverse()
