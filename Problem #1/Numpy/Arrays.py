import numpy

def arrays(arr):
    arr.reverse()  # Reverse the list
    return numpy.array(arr, float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)