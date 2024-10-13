import numpy as np

N, M = map(int, input().split())
matrix = np.array([list(map(int, input().split())) for _ in range(N)])
print(np.transpose(matrix))
print(matrix.flatten())


