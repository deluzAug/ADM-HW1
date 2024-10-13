#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr

def insertionSort1(x, Arr):
    value = Arr[x-1]
    for i in range(x-2, -1, -1):
        if Arr[i] >= value:
            Arr[i+1] = Arr[i]
        elif Arr[i] < value:
            Arr[i+1] = value
            return Arr
            break
        if i == 0:
            Arr = [value] + Arr[1:x]
            return Arr
            break

def insertionSort2(n, arr):
    # we create the list to be updated with every iteration
    ordered = []
    
    for i in range(1, n):
        #we skip the case of a list of just one value
        selector = i+1
        #we take the first i elements of arr and then use our previous function to sort them
        to_order = arr[0:selector]
        ordered = insertionSort1(i+1, to_order) + arr[selector:n+1]
        # we modify arr keeping track of the changes and then print the list
        arr = ordered
        print(*ordered)
        
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
