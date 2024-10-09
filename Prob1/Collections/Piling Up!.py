# Enter your code here. Read input from STDIN. Print output to STD
from collections import deque
for _ in range(int(input())):
    n = int(input())
    blocks = deque(map(int, input().split()))
    top_block = max(blocks[0], blocks[-1])
    success = True
    for _ in range(n):
        if blocks[0] >= blocks[-1] and top_block >= blocks[0]:
            top_block = blocks.popleft()
        elif blocks[-1] >= blocks[0] and top_block >= blocks[-1]:
            top_block = blocks.pop()
        else:
            print('No')
            success = False
            break
    if success:
        print('Yes')
            
    