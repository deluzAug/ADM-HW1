# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
for i in range(int(input())):
    command, *value = input().split()
    if value != []:
        exec(f"d.{command}(int({value}[0]))")
    else:
        exec(f"d.{command}()")
print(*d)
