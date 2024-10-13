# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = r"(7|8|9)(\d{9})$"
N = int(input())
Number_list = [input() for _ in range(N)]

for i in range(len(Number_list)):
    match = re.match(pattern, Number_list[i])
    if match:
        print('YES')
    else:
        print('NO')