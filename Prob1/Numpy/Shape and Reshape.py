import numpy

original_list = list(map(int, input().split()))
print(numpy.reshape(original_list, (3, 3)))

# forgot to convert the list into a numpy array but in this case it's not necessary...