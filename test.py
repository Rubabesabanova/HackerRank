def solve(s):
    s=s.capitalize()
    str_list=list(s)
    for i in range(len(str_list)):
        if i<len(str_list)-1:
            if str_list[i]==" " and str_list[i+1]!=" ":
                str_list[i+1]=str_list[i+1].upper()
    return "".join(str_list)
print(solve("hello   world  lol"))
