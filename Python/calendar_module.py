# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/calendar-module/problem
# Language : Python 3

import calendar
a=list(map(int, input().split()))
weekdict={0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4:"Friday", 5: "Saturday", 6: "Sunday"}
print(weekdict[calendar.weekday(a[2], a[0], a[1])].upper())