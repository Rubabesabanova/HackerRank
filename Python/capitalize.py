# Difficulty : Easy
# Link : https://www.hackerrank.com/challenges/capitalize/problem
# Language : Python 3

def solve(s):
    str_list=list(s.capitalize())
    for i in range(len(str_list)):
        if i<len(str_list)-1:
            if str_list[i]==" " and str_list[i+1]!=" ":
                str_list[i+1]=str_list[i+1].upper()
    return "".join(str_list)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()