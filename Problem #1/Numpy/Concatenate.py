import numpy as np
# I'll use the np abbreviation in every exercise, it's an habit

N, M, P = map(int, input().split())

matrix_a = np.array([list(map(int, input().split())) for _ in range(N)])

matrix_b = np.array([list(map(int, input().split())) for _ in range(M)])

print(np.concatenate((matrix_a, matrix_b), axis = 0 ))
