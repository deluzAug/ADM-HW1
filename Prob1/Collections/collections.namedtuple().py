# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N, student =int(input()), namedtuple('student', input())
St_List = [student(*input().split()) for i in range(N)]
print(sum([int(student.MARKS) for student in St_List])/N)
