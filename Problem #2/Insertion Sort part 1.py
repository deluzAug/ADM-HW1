#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    value = arr[n-1]
    for i in range(n-2, -1, -1):
        if arr[i] >= value:
            arr[i+1] = arr[i]
            print(*arr)
        elif arr[i] < value:
            arr[i+1] = value
            print(*arr)
            break
        if i == 0:
            arr = [value] + arr[1:n]
            print(*arr)
            break
    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
