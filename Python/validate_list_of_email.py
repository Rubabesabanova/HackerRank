# Difficulty : Medium
# Link : https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
# Language : Python 3

import re

def fun(s):
    x=re.search(r"^[\w-]+@[a-zA-Z0-9]+\.(.{,3})$", s)
    return True if x else False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)