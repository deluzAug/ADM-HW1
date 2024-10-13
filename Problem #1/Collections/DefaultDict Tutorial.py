from collections import defaultdict
N, M = list(map(int, input().split()))
A = defaultdict(list)
for i in range(N):
    A[input()].append(i+1)

for i in range(M):
    b = input()
    if A[b] == []:
        print(-1)
    else:
        print(*A[b])
    
