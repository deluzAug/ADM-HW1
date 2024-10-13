# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
Countries = set()
for i in range(N):
    Countries.add(input())

print(len(Countries))
