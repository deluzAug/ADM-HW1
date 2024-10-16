#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    k1_pos = x1
    k2_pos = x2
    # start a loop to see if they'll ever meet
    while True:
        k1_pos += v1
        k2_pos += v2
        if k1_pos == k2_pos:
            return 'YES'
            break
        # check if the fastest kangaroo has surpassed the other
        elif v1 >= v2 and k1_pos > k2_pos:
            return 'NO'
            break
        elif v2 >= v1 and k2_pos > k1_pos:
            return 'NO'
            break
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()