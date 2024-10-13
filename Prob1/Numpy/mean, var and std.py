import numpy as np

n, m = map(int, input().split())

array = [input().split() for _ in range(n)]
matrix = np.array(array, float)

print(np.mean(matrix, axis = 1))
print(np.var(matrix, axis = 0))
#my output produces more digits than the expected output, so I have to round it...
print(round(np.std(matrix),11))

