# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/alphabet-rangoli/problem
# Language : Python 3

def print_rangoli(size):
    ascii_number=96+size
    whole_letters=[]
    for i in range(0, size):
        letters=[]
        k=0
        while i>=k:
            letters.append(chr(ascii_number-k))
            k+=1
        for i in range(len(letters)-2, -1, -1):
            letters.append(letters[i])
        whole_letters.append(letters)
    for i in range(len(whole_letters)-2, -1, -1):
            whole_letters.append(whole_letters[i])

    for i in range(len(whole_letters)):
        line=""
        main_pattern="-".join(whole_letters[i])
        line=main_pattern.center((size*2-1)*2-1, "-")
        print(line)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)