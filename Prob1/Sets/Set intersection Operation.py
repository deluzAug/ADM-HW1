# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
List_eng = set(map(int, input().split()))
b = int(input())
List_french = set(map(int, input().split()))
print(len(List_eng & List_french))

