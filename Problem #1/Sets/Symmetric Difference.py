M = input()
a = set(input().split())
N = input()
b = set(input().split())

diff = a.union(b) - a.intersection(b)
diff = list(map(int, diff))
[print(i) for i in sorted(diff)]

