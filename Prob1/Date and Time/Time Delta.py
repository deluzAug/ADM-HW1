#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime


def time_delta(t1, t2):
    # Define the date format to parse the timestamps
    format_date = "%a %d %b %Y %H:%M:%S %z"

    # Create datetime objects for both timestamps directly
    date1 = datetime.strptime(t1, format_date)
    date2 = datetime.strptime(t2, format_date)

    # Calculate the absolute difference in seconds, gives a float
    delta = abs((date1 - date2).total_seconds())

    # Return the result as a string with no decimals
    return f"{delta:.0f}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()