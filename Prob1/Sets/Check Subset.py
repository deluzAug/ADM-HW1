# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    n_A = input()
    A = set(map(int, input().split()))
    n_B = input()
    B = set(map(int, input().split()))
    
    if A == A.intersection(B):
        print(True)
    else:
        print(False)
