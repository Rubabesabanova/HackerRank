n = int(input())
s = set(map(int, input().split()))
number_commands=int(input())
for i in range(number_commands):
    i=input().split()
    print(i)
    if i[0]=="pop":
        s.pop()
    elif i[0]=="remove":
        s.remove(int(i[1]))
    elif i[0]=="discard":
        s.discard(i[1])
