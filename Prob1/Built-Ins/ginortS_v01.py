# Enter your code here. Read input from STDIN. Print output to STDOUT
lower_case_letters =[]
upper_case_letters =[]
even_dig = []
odd_dig =[]

for i in input():
    if i.isalpha() and i.islower():
        lower_case_letters.append(i)
    elif i.isalpha() and i.isupper():
        upper_case_letters.append(i)
    elif i.isdecimal() and int(i)% 2 ==0:
        even_dig.append(i)
    else:
        odd_dig.append(i)


commands = ["''.join(sorted(lower_case_letters))", "''.join(sorted(upper_case_letters))", "''.join(sorted(odd_dig))", "''.join(sorted(even_dig))"]
sorted_list = [eval(i) for i in commands]
print(''.join(sorted_list))

#This is probably too complicated, but it works... 