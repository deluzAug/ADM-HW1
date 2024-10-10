# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
set_eng = set(map(int, input().split()))
b = input()
set_french = set(map(int, input().split()))

print(len(set_eng ^ set_french))
