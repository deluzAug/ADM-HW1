Set_A = set(map(int, input().split()))
N = int(input())
result = True
for i in range(N):
    Set_B = set(map(int, input().split()))
    if len(Set_B) > len(Set_A):
        result = False
    elif Set_B.intersection(Set_A) != Set_B:
        result = False

print(result)
