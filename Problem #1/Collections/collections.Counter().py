
from collections import Counter
X = int(input())
shoes = list(map(int, input().split()))
shoes_dict = Counter(shoes)
N = int(input())
total = 0
for i in range(N):
    shoe_size, prize = list(map(int, input().split()))
    if shoe_size in shoes_dict.keys() and shoes_dict[shoe_size] != 0:
        total += prize
        shoes_dict[shoe_size] = shoes_dict[shoe_size] -1
    else:
        pass

print(total)
