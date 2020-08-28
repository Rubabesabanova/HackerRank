# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/whats-your-name/problem
# Language : Python 3

def print_full_name(a, b):
    print(f"Hello {first_name} {last_name}! You just delved into python.")


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
