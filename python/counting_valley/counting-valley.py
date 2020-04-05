
import math
import os
import random
import re
import sys

def countingValleys(n, s):
    sea_level = 0
    valley = 0
    for i in s:
        if i == 'U':
            sea_level += 1
        else:
            if sea_level == 0:
                valley += 1
            sea_level -= 1
    return valley
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
