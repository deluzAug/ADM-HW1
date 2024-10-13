# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
set_original = set(map(int, input().split()))
number_of_commands = int(input())
for i in range(number_of_commands):
    command, *leng = input().split()
    set_i = set(map(int, input().split()))
    eval(f"set_original.{command}({set_i})")

print(sum(set_original))
    