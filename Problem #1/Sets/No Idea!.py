n,m = input().split()
array = list(input().split())
A = set(input().split())
B = set(input().split())
score = 0
for i in array: 
    
    if i in A:
        score += 1
    if i in B:
        score += -1

print(score)
