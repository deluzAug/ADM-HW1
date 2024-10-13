import numpy as np

n, m = map(int, input().split())

array = [input().split() for _  in range(n)]
matrix = np.array(array, int)
print(np.prod(np.sum(matrix, axis = 0)))


