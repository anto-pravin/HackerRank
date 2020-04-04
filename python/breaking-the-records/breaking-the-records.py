#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max_count = 0
    min_count = 0
    maximum = scores[0]
    minimum = scores[0]
    for i in scores:
        if i > maximum:
            max_count += 1
            maximum = i
        if i < minimum:
            min_count += 1
            minimum = i
    return [max_count,min_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
