def swap_case(s):
    j = 0
    new_s = ''
    for i in s:
       if i.isupper():
           new_s += s[j].lower()
       elif i.islower():
           new_s += s[j].upper()
       else: 
           new_s += s[j]
       j +=1
    return(new_s)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)