#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    temp = set(arr)
    arr.sort()
    maximum = 0
    element = arr[0]
    for i in temp:
        if arr.count(i) > maximum:
            maximum = arr.count(i)
            element = i

    return element

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
