# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
eng = set(input().split())
b= input()
french = set(input().split())

union_set = eng.union(french)

print(len(union_set))
