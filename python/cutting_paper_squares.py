'''Mary has an  piece of paper that she wants to cut into  pieces according to the following rules:

She can only cut one piece of paper at a time, meaning she cannot fold the paper or layer already-cut pieces on top of one another.
Each cut is a straight line from one side of the paper to the other side of the paper. For example, the diagram below depicts the three possible ways to cut a  piece of paper:

Given  and , find and print the minimum number of cuts Mary must make to cut the paper into  squares that are  unit in size.

Input Format

A single line of two space-separated integers denoting the respective values of  and .


Output Format

Print a long integer denoting the minimum number of cuts needed to cut the entire paper into  squares.

Sample Input

3 1
Sample Output

2'''

import math
import os
import random
import re
import sys

def solve(n, m):
    return ((n-1)+(n*(m-1)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    result = solve(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
