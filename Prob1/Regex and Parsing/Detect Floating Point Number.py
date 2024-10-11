# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    string = input()
    patter = r"^[+-]?(\d+\.\d+|\.\d+)$"
    result = re.match(patter, string)
    try:
        if result:
            # Attempt to convert the matched result to float
            test = float(result.group())
            print(True)
        else:
            print(False)
    except ValueError: #the problem here can only rise from a valueError 
        print(False)
