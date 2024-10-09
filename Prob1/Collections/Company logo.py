#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


if __name__ == '__main__':
    s = input()
    dict_s = defaultdict(int)
    for i in s:
        dict_s[i] += 1
    
    for _ in range(3):
        keys_from_value = [(key, value) for key, value in dict_s.items() if value == max(dict_s.values())]
        keys_from_value = sorted(keys_from_value, key=lambda x: x[0])
        print(*keys_from_value[0])
        dict_s.pop(keys_from_value[0][0])
    