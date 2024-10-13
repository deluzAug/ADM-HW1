import numpy as np
N = int(input())
matrix = np.array([input().split() for _ in range(N)], float)

print(f"{round(np.linalg.det(matrix), 2)}")
