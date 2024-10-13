# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 

# I think I'll need to do this in two steps
N = int(input())

cards_to_check = [input().strip() for _ in range(N)] 

pattern = r'^(4|5|6)\d{3}(-?\d{4}){3}$'

# this checks that the string follows the right format, 4 groups of four digits separeted by '-' 

pattern_2 = r'(\d)\1{3,}'
# this looks for repetitions of four same digits
# testing this out in the case of the input: 5133-3367-8912-3456
# it doesn't catch the four subsequent 3 separated by the -
# so I need to eliminate the separators (line 25)


for i in cards_to_check:
    match = re.match(pattern, i)

    if match:
        
        i = re.sub(r"[ -]", "", i)
        
        match_four = re.findall(pattern_2, i)
        if match_four:
            print('Invalid')
        else:
            print('Valid')

    else:
        print('Invalid')


