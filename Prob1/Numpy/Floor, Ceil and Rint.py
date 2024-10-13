import numpy as np
np.set_printoptions(legacy='1.13')

array = np.array(input().split(), float)

print(np.floor(array))
print(np.ceil(array))
print(np.rint(array))
