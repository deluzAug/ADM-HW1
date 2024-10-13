#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    from collections import defaultdict
    # I'll use the defaultdict module
    heights = defaultdict(int)
    # This assigns value zero to each new key entry
    # Let's count the occurencies for every height
    for height in candles:
        heights[height] += 1
    # find the maximum key value
    highest = max(heights.keys())
    # return the corresponding highest value count
    return int(heights[highest])
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
