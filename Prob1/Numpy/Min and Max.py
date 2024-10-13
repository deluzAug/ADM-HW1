import numpy as np

n, m = map(int, input().split())

array = [input().split() for _ in range(n)]
matrix = np.array(array, int)
print(np.max(np.min(matrix, axis = 1)))
